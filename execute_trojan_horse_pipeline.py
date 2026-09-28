#!/usr/bin/env python3
"""
Trojan Horse Enterprise Campaign Automation Script
Vector One Holdings / Vector Institute
Generates targeted HRD Corp claimable outreach packages & pipeline tracking table for Top Malaysian PLCs & GLCs.
"""

import csv
import json
import os

TARGET_ACCOUNTS = [
    {
        "company": "Maybank",
        "sector": "Banking & Financial Services",
        "chro": "Chief Human Resources Officer",
        "cdo": "Chief Digital Officer",
        "headcount": 42000,
        "hrdf_budget": "RM 350,000+",
        "program": "Program A: Exec L4 Retreat",
        "trojan_upsell": "Vector Intelligence RMiT Agentic Customer Onboarding Automation ($250,000)"
    },
    {
        "company": "Sime Darby Berhad",
        "sector": "Industrial & Automotive",
        "chro": "Head of Group HR",
        "cdo": "Head of Digital Transformation",
        "headcount": 22000,
        "hrdf_budget": "RM 220,000+",
        "program": "Program B: Ops L2 Bootcamp",
        "trojan_upsell": "Vector Intelligence Supply Chain & Logistics Agentic Tracking ($180,000)"
    },
    {
        "company": "Sunway Group",
        "sector": "Real Estate & Healthcare",
        "chro": "Group Chief Human Resources Officer",
        "cdo": "Group CDO",
        "headcount": 16000,
        "hrdf_budget": "RM 180,000+",
        "program": "Program A: Exec L4 Retreat",
        "trojan_upsell": "Vector Intelligence Document Synthesis Hub ($200,000)"
    },
    {
        "company": "PETRONAS Digital",
        "sector": "Energy & Enterprise Tech",
        "chro": "Head of Learning & Leadership",
        "cdo": "VP of Digital",
        "headcount": 48000,
        "hrdf_budget": "RM 500,000+",
        "program": "Program B: Ops L2 Bootcamp",
        "trojan_upsell": "Vector Intelligence Refinery Telemetry Multi-Agent System ($300,000)"
    },
    {
        "company": "Axiata Group / CelcomDigi",
        "sector": "Telecommunications",
        "chro": "Chief People Officer",
        "cdo": "Chief Technology Officer",
        "headcount": 14000,
        "hrdf_budget": "RM 160,000+",
        "program": "Program B: Ops L2 Bootcamp",
        "trojan_upsell": "Vector Intelligence High-Volume Customer Care Agentic Gateway ($220,000)"
    },
    {
        "company": "Tenaga Nasional Berhad (TNB)",
        "sector": "Energy & Utilities",
        "chro": "Chief People Officer",
        "cdo": "Chief Information Officer",
        "headcount": 35000,
        "hrdf_budget": "RM 300,000+",
        "program": "Program A: Exec L4 Retreat",
        "trojan_upsell": "Vector Intelligence Smart Grid Dispatch Agent ($190,000)"
    }
]

def generate_trojan_horse_pipeline():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    summary_file = os.path.join(output_dir, "trojan_horse_pipeline_execution_summary.md")
    csv_file = os.path.join(output_dir, "trojan_horse_target_pipeline.csv")

    # Write CSV output for CRM / Sheets import
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "company", "sector", "chro", "cdo", "headcount", "hrdf_budget", 
            "program", "trojan_upsell"
        ])
        writer.writeheader()
        for acc in TARGET_ACCOUNTS:
            writer.writerow(acc)

    # Write Markdown Summary
    with open(summary_file, mode="w", encoding="utf-8") as f:
        f.write("# Trojan Horse Enterprise Pipeline Campaign Execution Summary\n\n")
        f.write("**Entity:** Vector Institute & Vector Intelligence\n")
        f.write("**Framework:** 100% HRD Corp (HRDF) SBL-Khas Claimable Strategy\n\n")
        f.write("--- \n\n")
        f.write("## 📊 Active Target Enterprise Pipeline Matrix\n\n")
        f.write("| Target Account | Sector | Est. HRDF Budget | Initial HRD Corp Program | Target Upsell Contract (Vector Intelligence) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        
        total_initial_hrdf = 0
        total_upsell_value = 0

        for acc in TARGET_ACCOUNTS:
            f.write(f"| **{acc['company']}** | {acc['sector']} | {acc['hrdf_budget']} | {acc['program']} | **{acc['trojan_upsell']}** |\n")
        
        f.write("\n---\n\n")
        f.write("## 🚀 High-Leverage Campaign Execution Milestones\n\n")
        f.write("1. **Outreach Dispatch:** Send CHRO email sequences for HRD Corp Claimable Bootcamps.\n")
        f.write("2. **eTRiS Approval:** Provide pre-filled SBL-Khas grant forms to target L&D teams.\n")
        f.write("3. **Bootcamp Delivery:** Deliver 2-Day Executive Retreat / 3-Day Ops Bootcamp.\n")
        f.write("4. **Workflow Audit:** Extract top 3 departmental operational bottlenecks during capstone.\n")
        f.write("5. **Conversion SOW:** Present Vector Intelligence Multi-Agent System Integration proposal ($150k–$300k value).\n")

    print(f"[SUCCESS] Trojan Horse Pipeline execution generated successfully at:\n - {summary_file}\n - {csv_file}")

if __name__ == "__main__":
    generate_trojan_horse_pipeline()
