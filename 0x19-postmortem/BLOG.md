# Postmortem: Web Stack Debugging Project Outage

## Issue Summary

**Duration:**  
Start: June 7, 2024, 10:00 AM (WAT)  
End: June 7, 2024, 12:30 PM (WAT)  

**Impact:**  
The main web application experienced a significant slowdown, leading to page load times increasing from an average of 1 second to over 30 seconds. Approximately 80% of users were affected, experiencing delays and intermittent timeouts. The user experience was severely impacted, leading to a high volume of customer complaints and potential loss of revenue.

**Root Cause:**  
The root cause was identified as a misconfigured database query that resulted in a full table scan, overloading the database server.

## Timeline

- **10:00 AM:** Issue detected via automated monitoring alerts indicating a sharp increase in response times.
- **10:05 AM:** On-call engineer receives an alert and begins initial investigation.
- **10:15 AM:** Preliminary checks on web server and application logs reveal no anomalies; database team is notified.
- **10:30 AM:** Database team begins examining query logs and performance metrics.
- **10:45 AM:** Misleading path: Cache servers checked for potential issues but found to be operating normally.
- **11:00 AM:** Escalated to senior database administrator due to continued high latency.
- **11:15 AM:** Detailed analysis of recent changes highlights a new database query deployed shortly before the issue began.
- **11:30 AM:** Query optimization attempted, but no significant improvement.
- **11:45 AM:** Rollback of the recent database changes initiated.
- **12:00 PM:** Performance metrics begin to normalize following the rollback.
- **12:30 PM:** Full service restored with normal response times confirmed.

## Root Cause and Resolution

**Root Cause:**  
The newly deployed database query was intended to improve data retrieval performance but was not properly indexed. This resulted in a full table scan whenever the query was executed, causing excessive load on the database server. The lack of an appropriate index led to the database server becoming overwhelmed, significantly slowing down the entire web application.

**Resolution:**  
The immediate resolution involved rolling back the problematic query to the previous version. Post-restoration, the query was reviewed and optimized by adding the necessary index. Extensive testing was conducted in a staging environment to ensure that the optimized query performed efficiently without causing additional load.

## Corrective and Preventative Measures

**Improvements and Fixes:**  
- Conduct a thorough review process for all database query changes.
- Implement more robust indexing strategies.
- Enhance monitoring to include specific alerts for query performance degradation.

**Tasks to Address the Issue:**
1. **Patch Nginx Server:** Update configurations to handle increased load gracefully.
2. **Add Monitoring on Server Memory:** Implement alerts for unusual memory usage patterns.
3. **Database Indexing:** Review and improve indexing on all frequently accessed tables.
4. **Query Performance Testing:** Establish a mandatory performance testing protocol for all new queries.
5. **Documentation:** Update internal documentation to include guidelines for query optimization and indexing best practices.
6. **Training:** Provide additional training for developers on efficient database querying and indexing techniques.

By addressing these areas, we aim to prevent similar incidents in the future and ensure that our system can handle changes more gracefully.
