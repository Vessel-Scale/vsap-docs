---
route: /assessment-scoring
tags:
  - library
  - scoring
  - assessment-definitions
  - results
---

# Assessment Scoring

Assessment scores are calculated based on respondent answers to questions and are presented using one of two chart types. Understanding how scores are calculated and displayed is critical for designing your assessment definitions.

## Scoring Overview

When respondents complete an assessment:

1. **Question responses are scored** based on the selected answers or numeric values
2. **Category scores are calculated** by combining scores from all questions in that category
3. **Overall assessment score** is computed from all category scores
4. **Results are displayed** using either a Gas Gauge or Bar Chart visualization

The key difference between scoring approaches is how the overall score is presented to respondents.

---

## Chart Types & Scoring Approaches

### Gas Gauge – Normalized Scoring

!!! note "PRESET: Gas Gauge"
    Gas Gauge is the default chart type and uses a normalized scoring approach.

**Gas Gauge converts your total score to a 1-5 Likert scale.**

The raw summed scores from all categories are mathematically converted to a 1-5 scale using this formula:

$$\text{Normalized Score} = \text{Sum of Category Scores} \times \frac{5}{\text{Maximum Possible Score}}$$

#### Key Characteristics

- **Normalized to 1-5 Scale**: All scores are displayed as a value between 1 and 5, regardless of how many questions are in the assessment
- **Percentage-Based Conversion**: Score reflects performance as a percentage of total possible points
- **Easier Comparison**: You can compare assessments with different numbers of questions using the same 1-5 scale
- **Intuitive Interpretation**: Similar to Likert scale ratings (1=Poor, 5=Excellent)

#### Example: Gas Gauge Scoring

**Assessment with 10 scorable questions (each worth 0-5 points)**

| Item | Value |
|------|-------|
| Total possible score | 50 points (10 questions × 5 max points each) |
| Your actual score | 35 points |
| Conversion factor | 5 ÷ 50 = 0.1 |
| **Normalized gas gauge score** | **35 × 0.1 = 3.5** |

Your result displays as **3.5 out of 5.0** on a gas gauge visualization.

#### Example: Gas Gauge vs. Different Assessment Sizes

**Assessment A: 5 questions (25 max points), your score: 20**
- Conversion: 5 ÷ 25 = 0.2
- Gas Gauge Score: 20 × 0.2 = **4.0**

**Assessment B: 10 questions (50 max points), your score: 40**
- Conversion: 5 ÷ 50 = 0.1
- Gas Gauge Score: 40 × 0.1 = **4.0**

Both assessments show **4.0 on the 1-5 scale**, even though the second has twice as many questions. This makes it easy to compare assessments of different lengths.

#### Visualization

The gas gauge visual shows:
- A circular gauge needle pointing to your position (1-5)
- Color coding (red=low, yellow=medium, green=high)
- Your score and maximum possible score
- Industry/business-size comparison indicator if available

---

### Bar Chart – Cumulative Scoring

!!! note "Alternative: Bar Chart"
    Bar Chart is an alternative chart type that uses cumulative scoring.

**Bar Chart displays your summed score without normalization.**

The scores from all categories are added together and displayed as a raw total, without conversion to a 1-5 scale.

$$\text{Cumulative Score} = \text{Sum of All Category Scores}$$

#### Key Characteristics

- **Raw Total Score**: Shows the actual sum of all question scores
- **Dependent on Assessment Size**: The maximum possible score varies based on the number of questions
- **Direct Comparison to Max**: You can easily see how far you are from the maximum possible score
- **Granular Detail**: Better for detailed analysis when you need to know the exact point total

#### Example: Bar Chart Scoring

**Assessment with 10 scorable questions (each worth 0-5 points)**

| Item | Value |
|------|-------|
| Total possible score | 50 points |
| Your actual score | 35 points |
| **Bar chart cumulative score** | **35 out of 50** |

Your result displays as a progress bar showing **35/50**, with the bar filled to 70%.

#### Example: Bar Chart with Different Assessment Sizes

**Assessment A: 5 questions (25 max points), your score: 20**
- Bar Chart Score: **20 out of 25**

**Assessment B: 10 questions (50 max points), your score: 40**
- Bar Chart Score: **40 out of 50**

Both assessments show 80% progress, but the raw numbers are different (20 vs. 40) because of the different assessment sizes. You must account for the different maximums when comparing.

#### Visualization

The bar chart visual shows:
- A horizontal progress bar
- Your cumulative score displayed in the bar
- The maximum possible score displayed to the right
- Industry/business-size comparison indicator (if available) shown as an arrow above the bar

---

## Comparison: Gas Gauge vs. Bar Chart

| Feature | Gas Gauge | Bar Chart |
|---------|-----------|-------------|
| **Scoring Approach** | Normalized to 1-5 scale | Raw cumulative total |
| **Formula** | Sum × (5 / Max) | Sum (no conversion) |
| **Scale** | Always 1-5 | Varies by assessment |
| **Easy Comparison** | Yes—all assessments use same scale | No—need to account for different maximums |
| **Best For** | Comparing different assessments | Detailed point-by-point analysis |
| **Interpretation** | Likert scale equivalent | Percentage of max possible |
| **Maximum Varies?** | No—always 5 | Yes—depends on question count |
| **Visualization** | Circular gauge needle | Horizontal progress bar |

---

## How Scores Are Calculated

### Step 1: Question Scoring

Each question is scored based on the respondent's answer:

**Multiple Choice & Multiple Select**
- Selected option's score value is assigned
- Example: Select "Strongly Agree" (score=5) on a Likert question

**Numeric Questions**
- The numeric value entered is the score
- Example: Enter "85" for "What percent of orders are on-time?"

**Numeric Range Questions**
- The numeric value is matched to a range, and that range's score is assigned
- Example: Enter "10" employees → matched to "1-20" range → score of 2

**Text Questions**
- Text questions are not scored (score = 0)
- Used for qualitative feedback only

### Step 2: Category Scoring

All question scores within a category are summed and averaged:

$$\text{Category Average Score} = \frac{\sum \text{All Question Scores in Category}}{\text{Number of Scorable Questions}}$$

### Step 3: Overall Assessment Score

All category scores are summed:

$$\text{Total Assessment Score} = \sum \text{All Category Average Scores}$$

### Step 4: Chart Type Conversion

Depending on the chart type:

**Gas Gauge**: Normalize to 1-5 scale
$$\text{Gas Gauge Score} = \text{Total Score} \times \frac{5}{\text{Maximum Possible Score}}$$

**Bar Chart**: Display raw total
$$\text{Bar Chart Score} = \text{Total Score (no conversion)}$$

---

## Practical Examples

### Example 1: Lean Manufacturing Assessment (Gas Gauge)

**Assessment Definition:**
- 3 categories with 5 questions each (15 total)
- Each question uses a 5-point Likert scale
- Maximum possible score: 75 (15 × 5)

**Results:**

| Category | Questions | Average Score | Category Total |
|----------|-----------|----------------|-----------------|
| Lean Principles | 5 | 4.2 | 21 |
| Process Improvement | 5 | 3.8 | 19 |
| Continuous Improvement Culture | 5 | 4.0 | 20 |
| **TOTAL** | | | **60** |

**Gas Gauge Conversion:**
- Conversion factor: 5 ÷ 75 = 0.0667
- Normalized score: 60 × 0.0667 = **4.0**
- **Display: 4.0 out of 5.0** on the gas gauge

**Interpretation:** Strong performance on a 1-5 scale, equivalent to "Agree" on the Likert scale.

---

### Example 2: Supply Chain Maturity (Bar Chart)

**Assessment Definition:**
- 4 categories with 8 questions each (32 total)
- Mix of 4-point and 5-point scales, plus numeric range questions
- Maximum possible score: 128 (varies by question)

**Results:**

| Category | Points Earned | Max Points |
|----------|----------------|------------|
| Supply Chain Strategy | 28 | 32 |
| Supplier Management | 26 | 32 |
| Logistics & Distribution | 24 | 32 |
| Performance Metrics | 30 | 32 |
| **TOTAL** | **108** | **128** |

**Bar Chart Display:**
- **Score: 108 out of 128**
- Progress bar: 84% filled
- Industry average for this company size: 92 points (arrow indicator on bar)

**Interpretation:** You're above average for your company size, with particularly strong supply chain strategy and performance metrics.

---

## Selecting a Chart Type

When creating an assessment definition, choose a chart type based on your needs:

### Choose Gas Gauge if you:
- Want to compare assessments with different numbers of questions
- Prefer a simple 1-5 scale for interpretation
- Want results to be intuitive and easy to understand
- Are creating multiple assessment versions with different scopes
- Want to emphasize relative performance (percentage of maximum)

### Choose Bar Chart if you:
- Want to see the exact point total earned
- Are comparing the same assessment across multiple attempts
- Need to communicate detailed point-by-point progress
- Want respondents to understand how many points they earned toward the maximum
- Prefer a more granular view of achievement

---

## Related

- [Question Types](question-types.md)
- [Create Assessment Definition](create.md)
- [Edit Assessment Definition](edit.md)
