from client import EnterpriseAutonomousSupportTicketResolverClient

def main():
    client = EnterpriseAutonomousSupportTicketResolverClient()
    res = client.resolve_customer_incident('Customer requesting prorated enterprise license downgrade due to merger', 'ZENDESK_STRIPE')
    print('Support Incident: ' + res['resolution_session_id'] + ' | CRM: ' + res['crm_platform'])
    print('Root Cause: ' + res['root_cause_identified'])
    print('Actions: ' + ', '.join(res['autonomous_api_actions_executed']))
    print('Policy Passed: ' + str(res['deterministic_policy_compliance_passed']) + ' in ' + str(res['resolution_time_seconds']) + 's')
    print('Trace URL: ' + res['audit_trace_url'])

if __name__ == '__main__':
    main()
