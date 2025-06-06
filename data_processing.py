from fetch_data import fetch_data_creds, fetch_data_discovery
import pandas as pd
import streamlit as st

def process_astaka(df):
    df_astaka = df[df["bundle_name"] == "Astaka"].copy()
    df_astaka = df_astaka.sort_values(by=["id", "taken_date", "total_score"], ascending=[True, False, False])
    df_astaka["rank"] = df_astaka.groupby("id").cumcount() + 1
    df_astaka = df_astaka[df_astaka["rank"] <= 6]

    df_astaka_pivot = df_astaka.pivot(index=["id", "email", "name", "phone", "register_date"],
                                      columns="rank",
                                      values=["typology", "total_score"]).reset_index()

    df_astaka_pivot.columns = [
        f"Astaka_Top {col[1]}_{col[0]}" if isinstance(col, tuple) and col[1] else col[0]
        for col in df_astaka_pivot.columns
    ]

    df_astaka_date = df_astaka.groupby(["id", "email", "name", "phone", "register_date"])["taken_date"].max().reset_index()
    df_astaka_date.rename(columns={"taken_date": "Astaka_date"}, inplace=True)

    df_astaka_final = df_astaka_pivot.merge(df_astaka_date, on=["id", "email", "name", "phone", "register_date"], how="left")
    return df_astaka_final

def process_genuine(df):
    df_genuine = df[df["bundle_name"] == "Genuine"].copy()
    df_genuine = df_genuine.sort_values(by=["id", "taken_date", "total_score"], ascending=[True, False, False])
    df_genuine["rank"] = df_genuine.groupby("id").cumcount() + 1
    df_genuine = df_genuine[df_genuine["rank"] <= 9]

    df_genuine_pivot = df_genuine.pivot(index=["id", "email", "name", "phone", "register_date"],
                                        columns="rank",
                                        values=["typology", "total_score"]).reset_index()

    df_genuine_pivot.columns = [
        f"Genuine_Top {col[1]}_{col[0]}" if isinstance(col, tuple) and col[1] else col[0]
        for col in df_genuine_pivot.columns
    ]

    df_genuine_date = df_genuine.groupby(["id", "email", "name", "phone", "register_date"])["taken_date"].max().reset_index()
    df_genuine_date.rename(columns={"taken_date": "Genuine_date"}, inplace=True)

    df_genuine_final = df_genuine_pivot.merge(df_genuine_date, on=["id", "email", "name", "phone", "register_date"], how="left")
    return df_genuine_final

def process_others(df):
    bundle_names = ["GI", "LEAN", "ELITE"]
    df_list = []

    for bundle in bundle_names:
        df_bundle = df[df["bundle_name"] == bundle]

        df_final_result = df_bundle.pivot_table(
            index=["id", "email", "name", "phone", "register_date"],
            values="final_result",
            aggfunc="first"
        ).reset_index()
        df_final_result.rename(columns={"final_result": f"{bundle}_overall"}, inplace=True)

        df_typology = df_bundle.pivot_table(
            index=["id", "email", "name", "phone", "register_date"],
            columns=["test_name"],
            values="typology",
            aggfunc="first"
        )

        df_taken_date = df_bundle.pivot_table(
            index=["id", "email", "name", "phone", "register_date"],
            values="taken_date",
            aggfunc="first"
        ).reset_index()
        df_taken_date.rename(columns={"taken_date": f"{bundle}_date"}, inplace=True)

        df_typology.columns = [f"{bundle}_{col}" for col in df_typology.columns]
        df_typology = df_typology.reset_index()

        df_bundle_pivot = df_final_result.merge(df_taken_date, on=["id", "email", "name", "phone", "register_date"], how="left")
        df_bundle_pivot = df_bundle_pivot.merge(df_typology, on=["id", "email", "name", "phone", "register_date"], how="left")

        df_list.append(df_bundle_pivot)

    if df_list:
        df_final = df_list[0]
        for df_bundle_pivot in df_list[1:]:
            df_final = df_final.merge(df_bundle_pivot, on=["id", "email", "name", "phone", "register_date"], how="outer")
    else:
        df_final = pd.DataFrame()

    return df_final

def finalize_data():
    df_creds, df_links, df_b2b = fetch_data_creds()
    df_discovery = fetch_data_discovery()

    df_links["Tipologi"] = df_links["Tipologi"].str.strip()
    df_discovery["typology"] = df_discovery["typology"].str.strip()
    df_discovery["final_result"] = df_discovery["final_result"].str.strip()

    df_project = df_discovery[["id", "project"]].drop_duplicates().dropna(subset=["id"])

    df_others = process_others(df_discovery)
    df_astaka = process_astaka(df_discovery)
    df_genuine = process_genuine(df_discovery)

    on_cols = ["id", "email", "name", "phone", "register_date"]
    df_final = df_others.merge(df_astaka, on=on_cols, how="outer")
    df_final = df_final.merge(df_genuine, on=on_cols, how="outer")

    if "project" in df_final.columns:
        df_final = df_final.drop(columns=["project"])

    df_final = df_final.merge(df_project, on="id", how="left")

    column_order = [
        "id", "email", "name", "phone", "register_date", "project",
        "GI_date", "GI_overall", "GI_Creativity Style", "GI_Curiosity", "GI_Grit", "GI_Humility",
        "GI_Meaning Making", "GI_Mindset", "GI_Purpose in Life",
        "LEAN_date", "LEAN_overall", "LEAN_Cognitive Flexibility", "LEAN_Intellectual Curiosity", "LEAN_Open-Mindedness",
        "LEAN_Personal Learner", "LEAN_Self-Reflection", "LEAN_Self-Regulation", "LEAN_Social Astuteness",
        "LEAN_Social Flexibility", "LEAN_Unconventional Thinking",
        "ELITE_date", "ELITE_overall", "ELITE_Empathy", "ELITE_Motivation", "ELITE_Self-Awareness",
        "ELITE_Self-Regulation", "ELITE_Social skills",
        "Astaka_date", "Astaka_Top 1_typology", "Astaka_Top 1_total_score", "Astaka_Top 2_typology",
        "Astaka_Top 2_total_score", "Astaka_Top 3_typology", "Astaka_Top 3_total_score",
        "Astaka_Top 4_typology", "Astaka_Top 4_total_score", "Astaka_Top 5_typology",
        "Astaka_Top 5_total_score", "Astaka_Top 6_typology", "Astaka_Top 6_total_score",
        "Genuine_date", "Genuine_Top 1_typology", "Genuine_Top 1_total_score", "Genuine_Top 2_typology",
        "Genuine_Top 2_total_score", "Genuine_Top 3_typology", "Genuine_Top 3_total_score",
        "Genuine_Top 4_typology", "Genuine_Top 4_total_score", "Genuine_Top 5_typology",
        "Genuine_Top 5_total_score", "Genuine_Top 6_typology", "Genuine_Top 6_total_score",
        "Genuine_Top 7_typology", "Genuine_Top 7_total_score", "Genuine_Top 8_typology",
        "Genuine_Top 8_total_score", "Genuine_Top 9_typology", "Genuine_Top 9_total_score"
    ]

    df_final = df_final[[col for col in column_order if col in df_final.columns]]
    
    df_final["project"] = df_final["project"].replace(
    "Discover Your Learning Agility to Adapt and Succeed in a Fast-Paced World - Universitas Kristen Petra", 
    "UKPFEB25")

    df_final["project"] = df_final["project"].replace(
    "[Kenali Karakteristik Diri, Siap Berkreasi dan Berinovasi- Universitas Kristen Petra]", 
    "UKPMEI25")

    return df_creds, df_links, df_b2b, df_final
