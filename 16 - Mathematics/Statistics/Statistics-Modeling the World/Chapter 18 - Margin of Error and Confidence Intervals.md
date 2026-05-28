

# CI, ME, and Sample Size relationships

## 🔹 Relationships

- Confidence ↑ → ME ↑
- Sample size ↑ → ME ↓
- Sample size ↑ → Confidence ↑ (if ME fixed)
- To cut ME in half → need **4× n**

# 🔹 One-line memory version

> “More confidence = wider interval, more data = tighter interval, and shrinking error is expensive (needs 4× data)”

# 🔹 Intuition anchor

- Want to be **more sure** → widen the net
- Want to be **more precise** → collect more data
- Want **half the error** → pay 4× the data cost

# Constructing a CI

Identify variables.

Need $p$, $q$, $n$.

Find ME

Find SE

Apply the ME to the sample estimate (proportion or mean).


# Finding Sample Size from Confidence level and ME

$$
n=\left( \frac{z^*}{ME} \right)^2 *p(1-p)
$$

or

$$
n=\frac{pq}{\left( \frac{ME}{z^*} \right)^2}
$$
