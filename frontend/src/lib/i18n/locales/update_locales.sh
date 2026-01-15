#!/bin/bash
# Add missing keys to each locale file

for file in es.ts fr.ts it.ts ja.ts ko.ts ar.ts da.ts pt.ts; do
  # Add common keys
  sed -i "s/retry: '.*',$/retry: '\0'\n    country: 'Country',\n    state: 'State',\n    city: 'City',\n    selectState: 'Select state',\n    searchCity: 'Search city...',\n    switchTheme: 'Switch theme',\n    selectTheme: 'Select Theme',/" "$file" 2>/dev/null || true
done
