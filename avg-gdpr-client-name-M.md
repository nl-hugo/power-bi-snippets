
## Obfuscate client name for AVG/GDPR compliance (M-formula)

Helps making your Power BI reports AVG compliant by obfuscating client names and other sensitive fields by keeping only the first 3 characters followed by a fixed number of `*` symbols.

    = Table.AddColumn(Source, "Name (AVG)", each Text.Start([name], 3) & Text.Repeat("*", 9), type text)
