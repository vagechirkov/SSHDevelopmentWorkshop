library(brms)

fit1 <- brm(count ~ zAge + zBase * Trt + (1|patient),
            data = epilepsy, family = poisson())

summary(fit1)

plot(fit1, variable = c("b_Trt1", "b_zBase"))
