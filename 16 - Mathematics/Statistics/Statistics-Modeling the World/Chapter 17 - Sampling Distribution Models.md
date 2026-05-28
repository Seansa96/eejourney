

From any one random sample, the best guess of the true proportion is the observed sample proportion.  However, since each sample is different, one has to account for that and estimate how good that guess is.

The distribution of the proportions from all possible samples is called the sampling distribution of the proportion.  

# Notation

$p$ - probability of success
$\hat{p}$ - observed proportion in a sample
$q$- probability of a failure. (1-p)
$\hat{q}$ - observed value of the probability of a failure


# Standard Deviation of a sampling distribution

$$
SD(\hat{p})=\sqrt{ \frac{pq}{n} }
$$
This is the standard deviation not of the data, but of the proportions of all possible samples of $n$ values from the population.

## Example 1

What is the standard deviation of the sampling distribution where $p=11.6$ and the sample size is 100?

> [!answer]- Answer
> ![[Pasted image 20260409155457.png]]



# Sampling Error

Because we associate this distribution with a normal model, we can use the 68-95-99.7% rule, meaning that we can expect variability within the range of samples, but we just wouldn't expect *too* much variability.

In that sense, it isn't actually error at all, but the variability it suggests.


# When can we use a Normal model

The Normal model becomes a better and better approximation of the sampling distribution as the sample size increases.  Populations with a true proportion that is very small--close to 0 or 1--will always present an issue and won't function well with the Normal model, as no matter how large our sample size gets.


## Assumptions

**Independence:** The individuals in the sample must be independent of each other. 

**Randomization Condition**: Sample should be a random sample of the population

**10% Condition**: If your sample represents a large fraction of the population, then the Normal model may not be reasonable. Once you've sample more than about 10% of the population, the remaining individuals are no longer really independent of each other.

**Sample Size Assumption:** The sample size, $n$, must be large enough, relative to $p$. The closer to 0 or 1 that $p$ is, the larger $n$ must be.

**Success/Failure Condition:** The sample size must be large enough that we expect to see at least 10 successes and at least 10 failures ($np \geq 10$ and $nq \geq 10$).



# Finding the area to the right of z


* Does it satisfy the conditions to use a normal model? Ask: Is it random, and is it less than 10% of the population?
* Check if it passes success/failure condition. Do np and nq and check if both are $\geq$ 10.
* If not explicitly given the probability that is desired (like, they give you x out n instead of "we want 95%"), find it using simple math (ex: 23/728 * 100. The times 100 is optional though since you only need $P$)
* Get std deviation for sampling distribution. Then, subtract $p$ from $\hat{p}$ and divide that by the std deviation to get the z-score
* Then, just use tech to find the area to the right or left of z. Guide on that below. But yeah, that's your answer.

## Ti-83 Finding area to the right or left of $z$.

* Hit 2nd, then hit VARS to enter DISTR.
* Select normalcdf
* Enter z-score value (ex: should be something like 1.21)
* Hit comma to separate next value.
* Enter in infinity which is
* Type 1
* Hit 2nd, then hit comma which will enter in EE
* Then type 99
* Close the parentheses of the normalcdf function
* Hit enter, and that's your area.

This is for the RIGHT of Z, if you're looking for the area to the LEFT of z, switch the z-score with infinity, and make it negative infinity.

So:

$$
normalcdf(-\infty,1.21)
$$



# Finding a cutoff value given a probability (inverse normal)


* Convert to left
* Use invNorm on calculator, plug in the left $p$.
* Multiply by SE
* add the Mean


# Central Limit Theorem

If you take large enough random samples, the distribution of sample means (or proportions) becomes **approximately normal**, even if the original data isn’t.