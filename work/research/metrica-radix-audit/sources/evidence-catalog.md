# Evidence Catalog: MétricaRadix MCP Audit

## Source: MétricaRadix Repository (Primary)

| ID | Source | Type | Evidence Level | Key Finding |
|----|--------|------|----------------|-------------|
| S1 | `mcpfbads/src/server.py` | Primary (code) | Very High | 8 tools, multi-account via `list_ad_accounts()`, system user token auth |
| S2 | `mcpgoogleads/src/server.py` | Primary (code) | Very High | 10 tools, multi-account via `list_customers()`, MCC support via `LOGIN_CUSTOMER_ID` |
| S3 | `google-analytics-mcp/analytics_mcp/` | Primary (code) | Very High | 7 tools (incl. custom dims), property-based, ADC auth, coordinator pattern |
| S4 | `mcp-gsc/gsc_server.py` | Primary (code) | Very High | 19 tools, site-based, dual OAuth+service account auth |
| S5 | Root `.env` | Primary (config) | Very High | Shared credentials for FB + Google Ads; GA4 uses ADC separately |
| S6 | `mcpfbads/pyproject.toml` | Primary (config) | High | facebook-business>=24.0.0, mcp>=1.21.0 |
| S7 | `mcpgoogleads/pyproject.toml` | Primary (config) | High | google-ads>=28.0.0, mcp>=1.21.0 |
| S8 | `google-analytics-mcp/pyproject.toml` | Primary (config) | High | google-analytics-data==0.19.0, mcp[cli]>=1.2.0 |
| S9 | `mcp-gsc/pyproject.toml` | Primary (config) | High | google-api-python-client>=2.163.0, mcp[cli]>=1.3.0 |

## Key Claim Triangulation

### "Servers are already multi-account" (HIGH confidence)
- S1: `list_ad_accounts()` returns ALL accessible accounts, queries require `account_id` param
- S2: `list_customers()` returns all accessible customers, MCC fallback logic exists
- S3: `get_account_summaries()` returns all GA4 accounts/properties
- S4: `list_properties()` returns all GSC properties
- No hardcoded account IDs in any server (verified via grep)

### "Limitation is credential-level, not code-level" (HIGH confidence)
- S1: Facebook system user token determines accessible accounts (business manager scope)
- S2: Google Ads refresh token tied to one Google account (MCC can expand scope)
- S3: ADC credentials determine property access
- S5: Single `.env` file = single credential set = one user's universe of accounts
