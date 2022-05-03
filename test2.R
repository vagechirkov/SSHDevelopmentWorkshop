### Try to fit brms model
# Instructions to install brms package
# https://learnb4ss.github.io/learnB4SS/articles/install-brms.html#linux-1
library(brms)

fit1 <- brm(count ~ zAge + zBase * Trt + (1|patient),
            data = epilepsy, family = poisson())

summary(fit1)

plot(fit1, variable = c("b_Trt1", "b_zBase"))
