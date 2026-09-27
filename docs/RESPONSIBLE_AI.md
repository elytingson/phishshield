# Responsible AI

PhishShield is designed as a risk-based cybersecurity decision-support system.

## Principles

1. **No absolute safety claims**  
   A low phishing score does not prove that a URL is safe.

2. **Human oversight**  
   High-risk and uncertain cases should remain reviewable by an analyst.

3. **Safe feature collection**  
   The preferred production model uses URL-only features and does not require visiting the destination webpage.

4. **Explainability**  
   Provide risk score, risk tier, and principal contributing factors where feasible.

5. **Bias auditing**  
   Audit operational subgroups such as TLD frequency, URL length, HTTPS status, domain type, subdomain depth, and lexical complexity.

6. **No fabricated demographic fairness**  
   Do not compute or claim demographic fairness when demographic attributes are absent.

7. **Monitoring and drift**  
   Track score distribution, performance, calibration, false-positive rate, phishing recall, and subgroup performance over time.

8. **Versioning and rollback**  
   Keep model version, threshold, feature schema, and rollback capability.
