

domain_skill_map = {
    # ── Tech Domains ──────────────────────────────────────────────────────────
    "Web Development": [
        "HTML5", "CSS3", "JavaScript", "TypeScript", "React", "Next.js",
        "Vue.js", "Node.js", "Express.js", "REST API", "GraphQL",
        "Bootstrap", "Tailwind CSS", "Git", "Webpack", "Vite", "MongoDB",
        "PostgreSQL", "Redis", "Docker"
    ],
    "Data Science": [
        "Python", "R", "Pandas", "NumPy", "Matplotlib", "Seaborn",
        "Scikit-learn", "SQL", "Jupyter Notebook", "Tableau", "Power BI",
        "Excel", "Statistics", "A/B Testing", "Data Cleaning",
        "Feature Engineering", "BigQuery", "Spark", "Hadoop", "ETL"
    ],
    "Machine Learning": [
        "Python", "TensorFlow", "PyTorch", "Keras", "Scikit-learn",
        "XGBoost", "LightGBM", "NLP", "Computer Vision", "Deep Learning",
        "CNN", "RNN", "Transformers", "BERT", "Feature Engineering",
        "Model Deployment", "MLflow", "Hugging Face", "OpenCV", "CUDA"
    ],
    "Generative AI / LLMs": [
        "Prompt Engineering", "LangChain", "LlamaIndex", "OpenAI API",
        "Hugging Face", "RAG", "Vector Databases", "Pinecone", "ChromaDB",
        "Fine-tuning", "LoRA", "Embeddings", "Python", "FastAPI",
        "Streamlit", "LLM Evaluation", "LLM Safety", "Agents", "Tools/Function Calling", "RLHF"
    ],
    "Android Development": [
        "Java", "Kotlin", "XML", "Jetpack Compose", "Android Studio",
        "Firebase", "Room Database", "Retrofit", "MVVM", "LiveData",
        "ViewModel", "Navigation Component", "WorkManager", "Material Design",
        "Google Maps API", "Push Notifications", "Play Store Publishing",
        "Unit Testing", "Espresso", "Gradle"
    ],
    "iOS Development": [
        "Swift", "Objective-C", "SwiftUI", "UIKit", "Xcode",
        "Core Data", "Core Location", "AVFoundation", "Combine",
        "MVVM", "RESTful APIs", "Alamofire", "CocoaPods", "SPM",
        "TestFlight", "App Store Publishing", "ARKit", "CloudKit",
        "Push Notifications", "Unit Testing"
    ],
    "Flutter / Cross-Platform": [
        "Flutter", "Dart", "React Native", "JavaScript", "Firebase",
        "State Management", "Provider", "Riverpod", "Bloc", "GetX",
        "REST API", "SQLite", "Animations", "Material Design",
        "App Deployment", "iOS", "Android", "CI/CD", "Unit Testing", "Responsive UI"
    ],
    "DevOps / Cloud": [
        "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Terraform",
        "Ansible", "Jenkins", "GitHub Actions", "GitLab CI/CD",
        "Linux", "Bash Scripting", "Nginx", "Prometheus", "Grafana",
        "Helm", "ArgoCD", "IAM", "VPC", "Load Balancing"
    ],
    "Cloud Computing (AWS)": [
        "EC2", "S3", "Lambda", "RDS", "DynamoDB", "CloudFormation",
        "VPC", "IAM", "CloudWatch", "API Gateway", "ECS", "EKS",
        "Route 53", "SNS", "SQS", "Step Functions", "Cognito",
        "CDK", "Boto3", "Python"
    ],
    "Cybersecurity": [
        "Network Security", "Penetration Testing", "Ethical Hacking",
        "OWASP", "Kali Linux", "Nmap", "Metasploit", "Burp Suite",
        "SIEM", "Incident Response", "Threat Modeling", "Cryptography",
        "Firewalls", "VPN", "Zero Trust", "CISSP", "CEH", "SOC",
        "Vulnerability Assessment", "Python Scripting"
    ],
    "Software Engineering": [
        "OOP", "Data Structures", "Algorithms", "System Design",
        "Design Patterns", "Git", "Clean Code", "TDD", "Agile/Scrum",
        "REST API", "Microservices", "CI/CD", "Java", "C++", "Python",
        "SQL", "NoSQL", "Code Review", "Documentation", "Problem Solving"
    ],
    "Backend Development": [
        "Python", "Java", "Go", "Node.js", "Django", "FastAPI",
        "Spring Boot", "Express.js", "REST API", "GraphQL", "gRPC",
        "PostgreSQL", "MySQL", "MongoDB", "Redis", "RabbitMQ",
        "Kafka", "Docker", "JWT", "Microservices"
    ],
    "Full Stack Development": [
        "HTML", "CSS", "JavaScript", "React", "Node.js", "Express.js",
        "MongoDB", "PostgreSQL", "REST API", "Git", "Docker",
        "TypeScript", "Next.js", "Redux", "JWT", "AWS", "CI/CD",
        "Tailwind CSS", "GraphQL", "System Design"
    ],
    "UI/UX Design": [
        "Figma", "Adobe XD", "Sketch", "Wireframing", "Prototyping",
        "User Research", "Usability Testing", "Design Systems",
        "Accessibility (WCAG)", "Information Architecture", "User Personas",
        "A/B Testing", "Interaction Design", "Typography", "Color Theory",
        "Responsive Design", "Adobe Illustrator", "Zeplin", "InVision", "Framer"
    ],
    "Data Engineering": [
        "Python", "SQL", "Apache Spark", "Apache Kafka", "Airflow",
        "dbt", "Snowflake", "BigQuery", "Redshift", "ETL/ELT",
        "Data Warehousing", "Data Modeling", "AWS Glue", "Databricks",
        "Hadoop", "Hive", "Docker", "Git", "Terraform", "Data Quality"
    ],
    "Blockchain / Web3": [
        "Solidity", "Ethereum", "Web3.js", "Ethers.js", "Hardhat",
        "Truffle", "Smart Contracts", "DeFi", "NFTs", "IPFS",
        "MetaMask", "Chainlink", "React", "Node.js", "Rust",
        "Polkadot", "Solana", "Cryptography", "Gas Optimization", "Audit"
    ],
    "Game Development": [
        "Unity", "Unreal Engine", "C#", "C++", "Blueprints",
        "3D Modeling", "Game Physics", "AI (Game)", "Shader Programming",
        "Blender", "Game Design", "Multiplayer Networking",
        "UI/UX for Games", "AR/VR", "Mobile Gaming", "OpenGL",
        "DirectX", "Animation", "Level Design", "Performance Optimization"
    ],
    "Embedded Systems / IoT": [
        "C", "C++", "Python", "Arduino", "Raspberry Pi", "RTOS",
        "MQTT", "I2C", "SPI", "UART", "Firmware Development",
        "PCB Design", "Linux Kernel", "FreeRTOS", "Bluetooth/BLE",
        "Wi-Fi", "Zigbee", "Sensor Integration", "Edge Computing",
        "Low Power Design", "Assembly"
    ],
    "QA / Testing": [
        "Manual Testing", "Selenium", "Cypress", "Playwright",
        "JUnit", "PyTest", "Postman", "API Testing", "Load Testing",
        "JMeter", "TestNG", "BDD/Gherkin", "Cucumber", "Bug Reporting",
        "JIRA", "Test Case Design", "Regression Testing",
        "Performance Testing", "Mobile Testing", "CI/CD Integration"
    ],

    # ── Non-Tech / Business Domains ───────────────────────────────────────────
    "Digital Marketing": [
        "SEO", "SEM", "Google Ads", "Facebook Ads", "Content Marketing",
        "Email Marketing", "Social Media Marketing", "Analytics",
        "Google Analytics", "HubSpot", "Mailchimp", "Copywriting",
        "CRM", "A/B Testing", "Conversion Rate Optimization",
        "Affiliate Marketing", "Influencer Marketing", "Canva",
        "WordPress", "Marketing Automation"
    ],
    "Product Management": [
        "Product Roadmap", "Agile/Scrum", "User Stories", "JIRA",
        "Market Research", "Competitive Analysis", "Prioritization",
        "Stakeholder Management", "KPIs/OKRs", "A/B Testing",
        "Data Analysis", "SQL", "Wireframing", "Figma",
        "Go-to-Market Strategy", "Customer Discovery", "PRD Writing",
        "Confluence", "Product Analytics", "MVP Development"
    ],
    "Business Analyst": [
        "Requirements Gathering", "BRD / FRD Writing", "Use Case Diagrams",
        "Process Mapping", "SQL", "Excel", "Power BI", "Tableau",
        "Stakeholder Management", "JIRA", "Agile/Scrum", "Gap Analysis",
        "Data Analysis", "Visio", "UML", "SWOT Analysis",
        "Risk Analysis", "User Acceptance Testing (UAT)", "Documentation", "Communication"
    ],
    "Finance / Accounting": [
        "Financial Modeling", "Excel", "Tally ERP", "QuickBooks",
        "Accounting Principles (GAAP/IFRS)", "Tax Filing", "GST",
        "TDS", "Budgeting", "Forecasting", "Variance Analysis",
        "Balance Sheet", "P&L", "Cash Flow", "Audit",
        "Financial Reporting", "SAP FICO", "Python (Finance)",
        "Bloomberg Terminal", "Risk Management", "Valuation"
    ],
    "Human Resources (HR)": [
        "Recruitment", "Talent Acquisition", "Onboarding", "HRMS",
        "Payroll Processing", "Employee Relations", "Performance Management",
        "HR Policies", "Labor Laws", "Training & Development",
        "Succession Planning", "HRIS (SAP/Workday)", "Excel",
        "Communication", "Conflict Resolution", "Employer Branding",
        "Compensation & Benefits", "HR Analytics", "ATS Tools", "Compliance"
    ],
    "Content Writing / Copywriting": [
        "SEO Writing", "Blog Writing", "Copywriting", "Proofreading",
        "Content Strategy", "Research", "WordPress", "MS Word",
        "Social Media Content", "Email Newsletters", "Technical Writing",
        "Storytelling", "Grammarly", "Keyword Research", "Brand Voice",
        "Long-form Content", "Short-form Content", "Video Scripts",
        "Press Releases", "Content Calendar"
    ],
    "Graphic Design": [
        "Adobe Photoshop", "Adobe Illustrator", "Canva", "InDesign",
        "Typography", "Color Theory", "Branding", "Logo Design",
        "Print Design", "Social Media Graphics", "UI Design",
        "Figma", "Motion Graphics", "After Effects", "Video Editing",
        "Storyboarding", "Packaging Design", "Poster Design",
        "Photo Editing", "Visual Communication"
    ],
    "Teaching / Education": [
        "Curriculum Development", "Lesson Planning", "Classroom Management",
        "Differentiated Instruction", "Assessment Design", "MS PowerPoint",
        "Google Classroom", "Zoom/Online Teaching", "Communication",
        "Student Mentoring", "Subject Matter Expertise", "E-Learning Tools",
        "Moodle/LMS", "Parent Communication", "Report Writing",
        "Educational Psychology", "Special Education", "CBSE/ICSE/State Board",
        "Activity-Based Learning", "EdTech Tools"
    ],
}


def get_latest_skills(domain: str) -> list[str]:
    """Returns skill list for a given domain."""
    return domain_skill_map.get(domain, [])


def get_all_domains() -> list[str]:
    """Returns sorted list of all available domains."""
    return sorted(domain_skill_map.keys())