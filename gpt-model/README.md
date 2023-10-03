# Model assumptions

### Prompts

We assume the only inputs are inflation (%), income (GBP) and year, so prompts are of the form

```
Inflation: 5.4
Income: 45000
Year: 2022
```

### Completions

The completion will be annual spending habits in 4 categories

```
Food: 200
Transport: 1000
Clothing: 200
Entertainment: 200
```

### Training

Prompt training will therefore take this format

```json
{
  "prompt": "Inflation: 5.4, Income: 45000, Year: 2022",
  "completion": "Food: 200, Bills: 1000, Clothing: 200, Entertainment: 200"
}

```