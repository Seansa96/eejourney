
# P-value

For a right-tailed test:
normalcdf(zscore,1E99)

For a left-tailed test:
normalcdf(-1E99, zscore)

For a two-tailed test:
normalcdf(zscore, 1E99)* 2

Small P → Reject null hypothesis​; Large P → Fail to reject null hypothesis