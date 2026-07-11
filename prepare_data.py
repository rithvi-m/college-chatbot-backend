college_knowledge = [
    {
        "id": "about",
        "text": "Nehru Arts and Science College (NASC) is an Autonomous college affiliated to Bharathiar University, Coimbatore. It is NAAC accredited with A+ grade (CGPA 3.50), UGC recognized with 2(f) and 12-B status, ISO 9001:2015 certified, and ranked 101-150 by NIRF. It has around 3500 students."
    },
    {
        "id": "courses",
        "text": "NASC offers 27 Undergraduate, 08 Postgraduate, and 13 Research programmes across Arts, Life Science, Computational Sciences, Creative Sciences, Commerce, and Management. Popular UG courses include B.Sc Computer Science, B.Sc AIML and IoT, BCA, B.Com, BBA, and more."
    },
    {
        "id": "admission",
        "text": "Admissions for 2026 are open. Students can apply online through the college's official admission form, or download the brochure for full details. Required documents typically include 12th marksheet, transfer certificate, and community certificate."
    },
    {
        "id": "fees",
        "text": "Exact fee structure varies by course. For accurate fee details, students should contact the admission office directly or check the official fee page."
    },
    {
        "id": "placement",
        "text": "NASC has an active placement cell. Companies that have recruited from campus include TCS, Infosys, Cognizant, Paytm, CGVAK, and Zifq. Recently, 80 students from the 2026 batch were placed at RINEX with a package of 10 LPA."
    },
    {
        "id": "contact",
        "text": "NASC can be reached at nascoffice@nehrucolleges.com or by calling +91 887 000 5337. Address: Nehru Gardens, Thirumalayam Palayam, Coimbatore 641105."
    },
    {
        "id": "accreditation",
        "text": "NASC is NAAC accredited with A+ Grade (CGPA 3.50) in the III Cycle, UGC recognized (2(f) and 12-B), ISO 9001:2015 certified, and rated 4 Star by the Institution Innovation Council (IIC)."
    }
]

print(f"Loaded {len(college_knowledge)} knowledge chunks")
for item in college_knowledge:
    print(f"- {item['id']}")