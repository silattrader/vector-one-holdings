import csv
import json

b2b_customers = [
    # --- PILLAR 1: ANTI-UAV / COUNTER-DRONE (VECTOR AERO) ---
    {
        "ID": "AERO-01",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Civil Aviation Authorities & International Airports",
        "Industry Sector": "Aviation & Transportation",
        "Example Target Organizations": "Malaysia Airports Holdings Berhad (MAHB), Changi Airport Group (CAG), PT Angkasa Pura (Indonesia), Airports of Thailand (AOT)",
        "Economic Buyer (Authority)": "Director of Aviation Security / Chief Operating Officer (COO)",
        "Internal Champion": "Head of Airside Safety & Operations / Chief Security Engineer",
        "Primary Operational Pain Point": "Low-RCS drone incursions causing airport shutdown ($1M+/hour flight delay costs) and compliance with CAAM/ICAO airspace mandate",
        "Estimated Deal Value (USD)": "$500,000 - $2,500,000 TCV",
        "MEDDPICC Qualification Rule": "Must have active airport expansion or recent drone near-miss alert; budget >$500k",
        "Trigger Event / Catalyst": "CAAM drone security mandate update; airport expansion announcement; near-miss incident",
        "Value Proposition": "Unified Command Gateway integrating AESA micro-Doppler radar & RF jamming with sub-100ms automated response"
    },
    {
        "ID": "AERO-02",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Military & Armed Forces Air Defense",
        "Industry Sector": "Defense & National Security",
        "Example Target Organizations": "Malaysian Armed Forces (ATM), Singapore Armed Forces (SAF), TNI (Indonesia), Royal Thai Armed Forces",
        "Economic Buyer (Authority)": "Defense Procurement Director / Chief of Materiel",
        "Internal Champion": "Head of Air Defense Systems / Electronic Warfare Lead",
        "Primary Operational Pain Point": "Asymmetric drone swarm threats against forward military bases, ammo dumps, and naval ports",
        "Estimated Deal Value (USD)": "$1,000,000 - $10,000,000+ TCV",
        "MEDDPICC Qualification Rule": "Active defense budget procurement cycle; STANAG 4586 compliance requirement",
        "Trigger Event / Catalyst": "Regional defense budget allocation release; Joint exercises identifying C-UAS gaps",
        "Value Proposition": "Military-grade multi-spectral sensor fusion, tactical directional jamming & kinetic drone interception"
    },
    {
        "ID": "AERO-03",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Oil & Gas Refineries & Offshore Platforms",
        "Industry Sector": "Energy & Petrochemicals",
        "Example Target Organizations": "PETRONAS (Kerteh/Pengerang), Shell Malaysia, Pertamina (Indonesia), PTTEP (Thailand)",
        "Economic Buyer (Authority)": "VP of Health, Safety & Environment (HSE) / Head of Asset Protection",
        "Internal Champion": "Refinery Operations Director / Physical Security Manager",
        "Primary Operational Pain Point": "Aerial espionage, explosive drone attack risk on high-pressure gas/chemical storage tanks",
        "Estimated Deal Value (USD)": "$400,000 - $1,500,000 TCV",
        "MEDDPICC Qualification Rule": "High-hazard facility status; perimeter security budget allocated",
        "Trigger Event / Catalyst": "HSE perimeter risk audit failure; regional industrial security alert",
        "Value Proposition": "24/7 autonomous RF & optical perimeter surveillance with zero explosion-hazard ignition risks"
    },
    {
        "ID": "AERO-04",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Power Grids & Hydroelectric Power Stations",
        "Industry Sector": "Utilities & Infrastructure",
        "Example Target Organizations": "Tenaga Nasional Berhad (TNB), Sarawak Energy, PLN (Indonesia), Electricity Generating Authority of Thailand (EGAT)",
        "Economic Buyer (Authority)": "Chief Infrastructure Officer / VP of Transmission",
        "Internal Champion": "Substation Security Director / Grid Reliability Lead",
        "Primary Operational Pain Point": "Substation sabotage via payload-dropping drones causing blackout events affecting millions",
        "Estimated Deal Value (USD)": "$300,000 - $1,200,000 TCV",
        "MEDDPICC Qualification Rule": "Critical national infrastructure classification; multi-site deployment scope",
        "Trigger Event / Catalyst": "Government grid resilience mandate; smart grid modernization push",
        "Value Proposition": "Automated RF detection net providing early warning alerts across distributed power substations"
    },
    {
        "ID": "AERO-05",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Correctional Facilities & High-Security Prisons",
        "Industry Sector": "Government & Law Enforcement",
        "Example Target Organizations": "Malaysian Prisons Department (Jabatan Penjara Malaysia), Singapore Prison Service",
        "Economic Buyer (Authority)": "Director General of Prisons / Ministry of Home Affairs Procurement",
        "Internal Champion": "Prison Warden / Security Operations Superintendent",
        "Primary Operational Pain Point": "Contraband delivery (weapons, drugs, phones) over prison walls via commercial micro-drones",
        "Estimated Deal Value (USD)": "$200,000 - $800,000 TCV",
        "MEDDPICC Qualification Rule": "Active contraband smuggling via drone recorded; Ministry budget available",
        "Trigger Event / Catalyst": "Publicized contraband seizure; Ministry security audit",
        "Value Proposition": "Non-kinetic directional RF jamming shield isolating prison airspace 24/7 without disrupting emergency services"
    },
    {
        "ID": "AERO-06",
        "Pillar": "Vector Aero (Anti-UAV)",
        "Target Customer Segment": "Maritime Commercial Ports & Shipping Terminals",
        "Industry Sector": "Maritime & Logistics",
        "Example Target Organizations": "Port of Klang Authority, Port of Singapore Authority (PSA), Johor Port Berhad, Penang Port",
        "Economic Buyer (Authority)": "Head of Port Security / Chief Operations Officer",
        "Internal Champion": "Harbor Master / Port Facility Security Officer (PFSO)",
        "Primary Operational Pain Point": "Unsanctioned drone reconnaissance over container yards, oil tankers, and naval vessel docks",
        "Estimated Deal Value (USD)": "$400,000 - $1,800,000 TCV",
        "MEDDPICC Qualification Rule": "ISPS Code compliance requirement; heavy container traffic volume",
        "Trigger Event / Catalyst": "Port expansion; ISPS audit review; unauthorized vessel surveillance report",
        "Value Proposition": "Coastal AESA radar coverage combined with maritime-hardened C-UAS jammer pods"
    },

    # --- PILLAR 2: EVOMAX TOKEN ENGINE (VECTOR COMPUTE) ---
    {
        "ID": "COMP-01",
        "Pillar": "Vector Compute (EvoMax)",
        "Target Customer Segment": "B2B Generative AI SaaS Scale-ups",
        "Industry Sector": "Software & AI Tech",
        "Example Target Organizations": "Mindvalley, StoreHub, ServiceRocket, Supahands, regional AI writing & coding SaaS startups",
        "Economic Buyer (Authority)": "Chief Technology Officer (CTO) / VP of Engineering",
        "Internal Champion": "Lead AI Architect / Head of Infrastructure",
        "Primary Operational Pain Point": "Runaway LLM API costs ($30k–$150k/mo token burn) destroying software gross margins",
        "Estimated Deal Value (USD)": "$24,000 - $72,000 ACV ($2k-$6k/mo subscription)",
        "MEDDPICC Qualification Rule": "Monthly token spend >$20k/mo; p95 latency >1.2s; using OpenAI/Claude APIs",
        "Trigger Event / Catalyst": "Series A/B funding round; C-suite mandate to improve gross margins; API rate-limit bottlenecks",
        "Value Proposition": "Drop-in middleware cutting prompt token volume by 30-40% and reducing API latency by 120ms with 0 code changes"
    },
    {
        "ID": "COMP-02",
        "Pillar": "Vector Compute (EvoMax)",
        "Target Customer Segment": "Digital Banks & FinTech Platforms",
        "Industry Sector": "Banking & Financial Technology",
        "Example Target Organizations": "Touch 'n Go Digital, Grab Financial Group, GXBank, Boost Bank, Wise ASEAN, Revolut",
        "Economic Buyer (Authority)": "Chief Information Officer (CIO) / Head of Financial Tech Infrastructure",
        "Internal Champion": "Principal LLM Engineer / Lead Data Scientist",
        "Primary Operational Pain Point": "High cost and high latency when processing million-token financial documents and automated compliance checks",
        "Estimated Deal Value (USD)": "$48,000 - $120,000 ACV",
        "MEDDPICC Qualification Rule": "High query volume; strict data sovereignty compliance required; active LLM feature scaling",
        "Trigger Event / Catalyst": "Launch of AI financial advisor / customer agent; quarterly COGS audit",
        "Value Proposition": "On-premise / VPC-deployable EvoMax token compression with Zero-Data-Retention SLA"
    },
    {
        "ID": "COMP-03",
        "Pillar": "Vector Compute (EvoMax)",
        "Target Customer Segment": "Customer Service & Contact Center AI Providers",
        "Industry Sector": "Telecommunications & Customer Experience",
        "Example Target Organizations": "Teleperformance Malaysia, Concentrix ASEAN, Agmo Holdings, Daythree Tech, Teledirect",
        "Economic Buyer (Authority)": "Chief Digital Officer (CDO) / VP of Customer Experience Tech",
        "Internal Champion": "Head of Automation / Conversational AI Product Lead",
        "Primary Operational Pain Point": "API latency spikes during live customer chat interactions causing user drop-off & high cost per resolved ticket",
        "Estimated Deal Value (USD)": "$36,000 - $96,000 ACV",
        "MEDDPICC Qualification Rule": ">100k daily chat sessions; real-time streaming requirements",
        "Trigger Event / Catalyst": "Omnichannel AI migration project; contract renewal with legacy chatbot vendor",
        "Value Proposition": "Sub-50ms proxy compression overhead providing instant SSE stream acceleration and 35% token savings"
    },
    {
        "ID": "COMP-04",
        "Pillar": "Vector Compute (EvoMax)",
        "Target Customer Segment": "HealthTech & Telemedicine AI Assistants",
        "Industry Sector": "Healthcare & Life Sciences",
        "Example Target Organizations": "DoctorOnCall, Naluri, Speedoc, BookDoc, HealthifyMe ASEAN",
        "Economic Buyer (Authority)": "Chief Medical Information Officer (CMIO) / CTO",
        "Internal Champion": "Lead Health Data Architect",
        "Primary Operational Pain Point": "High token costs for parsing long medical transcripts and EHR histories while maintaining strict privacy SLA",
        "Estimated Deal Value (USD)": "$30,000 - $84,000 ACV",
        "MEDDPICC Qualification Rule": "Processes medical records via LLMs; requires RAM-only non-persistent processing",
        "Trigger Event / Catalyst": "Telehealth user volume surge; HIPAA/PDPA compliance audit",
        "Value Proposition": "RAM-only semantic context compression preserving medical entity accuracy while lowering inference bills"
    },

    # --- PILLAR 3: MINIMAX / ANTHROPIC / GOOGLE AI RESELLING (VECTOR COMPUTE) ---
    {
        "ID": "RESELL-01",
        "Pillar": "Vector Compute (Token Logistics)",
        "Target Customer Segment": "Enterprise AI Research Labs & Universities",
        "Industry Sector": "Education & Deep-Tech Research",
        "Example Target Organizations": "Universiti Malaya AI Centre, NTU Singapore, NUS AI Institute, MIMOS Berhad",
        "Economic Buyer (Authority)": "Dean of Research / Director of High-Performance Computing",
        "Internal Champion": "Lead AI Researcher / Compute Allocation Manager",
        "Primary Operational Pain Point": "Unstable credit limits, lack of local billing/tax invoicing, and rate limits on global API accounts",
        "Estimated Deal Value (USD)": "$50,000 - $300,000 Annual Token Volume",
        "MEDDPICC Qualification Rule": "Requires high-throughput dedicated channels; localized SST/GST invoicing",
        "Trigger Event / Catalyst": "Government research grant award; new AI research initiative announcement",
        "Value Proposition": "SLA-backed MiniMax & frontier LLM token distribution with local invoice billing and dedicated throughput support"
    },
    {
        "ID": "RESELL-02",
        "Pillar": "Vector Compute (Token Logistics)",
        "Target Customer Segment": "Enterprise Software Systems Integrators & MSPs",
        "Industry Sector": "IT Services & Enterprise Consulting",
        "Example Target Organizations": "Axiata Digital Labs, TM One (Telekom Malaysia), Maxis Enterprise, HeiTech Padu",
        "Economic Buyer (Authority)": "VP of Cloud & AI Solutions / Head of Partner Ecosystems",
        "Internal Champion": "Enterprise Solutions Architect",
        "Primary Operational Pain Point": "Inability to resell foundation model tokens to government/corporate clients due to lack of wholesale distribution margin",
        "Estimated Deal Value (USD)": "$100,000 - $500,000 Annual Partner Revenue",
        "MEDDPICC Qualification Rule": "Existing MSP client base of 50+ enterprise accounts; active cloud migration contracts",
        "Trigger Event / Catalyst": "RFP submission requiring AI model integration; enterprise partner program review",
        "Value Proposition": "Wholesale token distribution pricing, white-label API proxy, and tier-1 partner margin share"
    },

    # --- PILLAR 4: APPLIED AI ACADEMY / VECTOR INSTITUTE (UPSKILLING) ---
    {
        "ID": "INST-01",
        "Pillar": "Vector Institute (Academy)",
        "Target Customer Segment": "Public Listed Companies (PLCs) with HRD Corp Funds",
        "Industry Sector": "Conglomerates & Diversified Holdings",
        "Example Target Organizations": "Sime Darby, Sunway Group, IOI Corporation, YTL Corporation, Gamuda Berhad",
        "Economic Buyer (Authority)": "Chief Human Resources Officer (CHRO) / Head of Learning & Development",
        "Internal Champion": "Head of Organizational Development / AI Center of Excellence Lead",
        "Primary Operational Pain Point": "Low employee AI tool adoption (<15%) despite procuring Microsoft Copilot / ChatGPT licenses; unutilized HRDF levy",
        "Estimated Deal Value (USD)": "$35,000 - $120,000 per Cohort (100% HRD Corp Claimable)",
        "MEDDPICC Qualification Rule": "Available HRDF levy balance >RM150k; employee headcount >500",
        "Trigger Event / Catalyst": "End-of-year HRDF levy balance expiration warning; C-suite mandate for AI adoption",
        "Value Proposition": "100% HRD Corp claimable Executive AI & Agentic Bootcamp certifying teams with 90%+ tool adoption rates"
    },
    {
        "ID": "INST-02",
        "Pillar": "Vector Institute (Academy)",
        "Target Customer Segment": "Commercial Banks & Financial Institutions",
        "Industry Sector": "Banking & Financial Services",
        "Example Target Organizations": "Maybank, CIMB Bank, RHB Bank, Hong Leong Bank, Public Bank, Bank Islam",
        "Economic Buyer (Authority)": "Head of Talent Development / Chief Transformation Officer",
        "Internal Champion": "Head of Digital Workforce / Business Unit HR Director",
        "Primary Operational Pain Point": "Skills gap among middle management in writing structured prompts, governance compliance, and agentic automation",
        "Estimated Deal Value (USD)": "$50,000 - $150,000 Enterprise Contract",
        "MEDDPICC Qualification Rule": "Active digital transformation program; strict regulatory data privacy standards",
        "Trigger Event / Catalyst": "BNM / Regulatory push for AI governance; annual employee upskilling calendar",
        "Value Proposition": "Role-specific AI training modules covering prompt engineering, agentic workflow logic, and financial compliance"
    },
    {
        "ID": "INST-03",
        "Pillar": "Vector Institute (Academy)",
        "Target Customer Segment": "Telecommunication & Technology Corporations",
        "Industry Sector": "Telecommunications",
        "Example Target Organizations": "CelcomDigi, Maxis, Time dotCom, U Mobile",
        "Economic Buyer (Authority)": "Chief People Officer (CPO) / VP of Technology Talent",
        "Internal Champion": "Director of Capability Building / Enterprise Agile Coach",
        "Primary Operational Pain Point": "Engineering and customer support staff lacking formal training on agentic AI frameworks and prompt optimization",
        "Estimated Deal Value (USD)": "$40,000 - $100,000 per Training Contract",
        "MEDDPICC Qualification Rule": "Over 1,000 technical employees requiring AI literacy certification",
        "Trigger Event / Catalyst": "Merger integration (e.g. CelcomDigi integration); launch of internal AI CoE",
        "Value Proposition": "Customized technical AI bootcamps with practical hands-on capstone projects applicable to telco workflows"
    }
]

# 1. Write to CSV file (Native Google Sheet importable format)
csv_file_path = r"C:\Users\User\Desktop\Vector One\Vector_One_Outputs\vector_one_logical_b2b_customers.csv"
fieldnames = list(b2b_customers[0].keys())

with open(csv_file_path, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(b2b_customers)

print(f"Successfully generated Google Sheet CSV file at: {csv_file_path}")
