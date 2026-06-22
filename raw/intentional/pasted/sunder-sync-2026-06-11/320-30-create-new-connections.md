---
type: raw_capture
source_type: web
title: "Sunder sync: 30-create_new_connections.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/30-create_new_connections.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/30-create_new_connections.md"
sha256: "1ff0fddc56ec1ac1712fe30796f60c9684e5fdd687374cf264ade5a6a916140b"
duplicate_of: ""
---

# Sunder sync: 30-create_new_connections.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/30-create_new_connections.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 30. create_new_connections

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "create_new_connections",
  "description": "Creates new connections to external services.\nDisplays a UI card where the user can choose to create each connection or skip it.\nCreating a connection will authenticate the user to the service and then save the connection to the user's account so they can use it in other agents in the future.\n\nIMPORTANT: You MUST read /agent/skills/system/creang-connections/SKILL.md for detailed setup instructions before using this tool.\n\nSupports the creation of 4 different types of connections: pre-built integrations, custom MCP, Direct API (HTTP) and Computer Use.\nFor pre-built integrations supports the creation of multiple connections at once. All others support only one connection creation at a time.\n\nFor each connection creation request returns:\n- userAction: 'created' if user authorized, 'skipped' if user declined.\n\nIf successfully created, also returns:\n- connectionId: the new connection ID. Don't mention the connectionId to the user.\n- tools: { activated: string[], deactivated: string[] } - list of all connection tool names by activation state\n- connection-specific details",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["connection"],
    "additionalProperties": false,
    "properties": {
      "connection": {
        "anyOf": [
          {
            "type": "object",
            "required": ["type", "integrations"],
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "const": "integrations",
                "description": "Create connections from pre-built integrations"
              },
              "integrations": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": ["integrationId"],
                  "additionalProperties": false,
                  "properties": {
                    "integrationId": {
                      "type": "string",
                      "description": "The integration id"
                    },
                    "toolsToActivate": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": "The list of tools to activate once the connection is created."
                    }
                  }
                },
                "description": "The list of integrations to create connections for."
              }
            }
          },
          {
            "type": "object",
            "required": ["type"],
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "const": "mcp",
                "description": "Create a connection to an MCP server"
              },
              "displayName": {
                "type": "string",
                "description": "A short human-readable display name for the MCP server"
              },
              "serverUrl": {
                "type": "string",
                "description": "The URL of the MCP server to connect to. Must have the https:// prefix. The user can edit or even completely rewrite the value during the setup."
              }
            }
          },
          {
            "type": "object",
            "required": ["type", "serviceName", "description", "connectionName", "baseUrl", "methods", "authConfig", "notes"],
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "const": "direct_api",
                "description": "Create a custom HTTP API connection"
              },
              "serviceName": {
                "type": "string",
                "description": "Name of the remote service (e.g., \"OpenAI API\", \"Stripe\")"
              },
              "description": {
                "type": "string",
                "description": "Clear description of what this service does"
              },
              "connectionName": {
                "type": "string",
                "minLength": 1,
                "maxLength": 32,
                "description": "Human-readable name (1-32 chars)"
              },
              "baseUrl": {
                "type": "string",
                "description": "The base URL of the API. Be extremely careful to find the correct base URL for the API."
              },
              "methods": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": ["GET", "POST", "PUT", "PATCH", "DELETE"]
                },
                "minItems": 1,
                "description": "HTTP methods to allow"
              },
              "authConfig": {
                "type": "object",
                "additionalProperties": {},
                "propertyNames": {
                  "type": "string"
                },
                "description": "Authentication config object. Read /agent/skills/system/creating-connections/create-direct-api-connection.md for schema."
              },
              "notes": {
                "type": "string",
                "description": "Markdown notes for this connection"
              },
              "testCases": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": {},
                  "propertyNames": {
                    "type": "string"
                  }
                },
                "maxItems": 3,
                "description": "Test cases to verify the API connection works. See skill file for schema."
              }
            }
          },
          {
            "type": "object",
            "required": ["type", "displayName"],
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "const": "computer_use",
                "description": "Provision a remote computer for browser or desktop UI use. This is expensive and slow."
              },
              "displayName": {
                "type": "string",
                "description": "A clear, purposeful display name for this computer (e.g., \"Development Computer\", \"Testing Computer\")."
              }
            }
          }
        ]
      }
    }
  }
}
```

