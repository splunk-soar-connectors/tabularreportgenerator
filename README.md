# Splunk> Phantom

Welcome to the open-source repository for Splunk> Phantom's tabularreportgenerator App.

Please have a look at our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md) if you are interested in contributing, raising issues, or learning more about open-source Phantom apps.

## Legal and License

This Phantom App is licensed under the Apache 2.0 license. Please see our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md#legal-notice) for further details.

# Tabular Report Generator 

The Tabular Report Generator (TRG) is a utility app for Splunk SOAR to generate tabular reports within playbooks to be delivered via the SMTP app.

## Installation

Please refer to the official Splunk SOAR documentation on how to install the app bundle on your platform.

## Provided Actions

- generate report email

## Configuration

If your report requires embedded images (eg. a banner or logo), create a new custom list and configure it under the TRG asset settings. If you don't need images inside your report, feel free to skip this.

The custom list must have two columns where the first one denotes the `cid` of the image (content id, must be unique in the list) and the second column must contain the image encoded in base64 format. It is recommended to use an external tool such as Excel to generate a CSV file following this format and to populate the custom list using the CSV upload functionality. 

## Report Specification

The **generate report email** action takes a `report_json` parameter as input which is defining the reports overall structure. The required input is a JSON with the following format eg:

```
{
    "message": "Intro Message",
    "rows": [{
        "type": "heading_row",
        "value": "My heading"
    }]
}
```

It is recommended to use an inline Code block inside your SOAR playbook to generate this input and not a Format block which requires cumbersome escaping when handling nested JSON.

### Row Types

Rows are entered in the `rows` key of the report specification. There are currently a number of row types supported. Every entry in the `rows` list corresponds to a row in the resulting report:

- `heading_row`: Visually highlighted row with centered text
    - **value**
- `text_row`: Single cell row
    - **value**
- `kv_row`: A row with a label cell and a larger content cell 
    - **key**: Label of the row
    - **value**: Contents of the row
- `lr_row`: 2 Equally spaced cells
    - **left**: Content of the left column
    - **right**: Content of the right column
- `image_row`: 
    - **cid**: content id reference to the configured custom list


#### Example
```
{
	"message": "hello",
	"rows": [{
    		"type": "image_row",
            "cid": "image_1"
          },
        {
			"type": "heading_row",
			"value": "Ticket Overview"
		},
        {
			"type": "kv_row",
			"key": "Key",
            "value": "Value"
		},
        {
            "type": "kv_row",
            "key": "another",
            "value": "one"
        }
	]
}
```
