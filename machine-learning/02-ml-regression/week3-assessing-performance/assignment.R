library(data.table)

train <- fread('data/wk3_kc_house_train_data.csv')
test <- fread('data/wk3_kc_house_test_data.csv')
valid <- fread('data/wk3_kc_house_valid_data.csv')

train$sqft_living <- as.numeric(train$sqft_living)
train[, power_1 := sqft_living]
train[, power_2 := sqft_living**2]
train[, power_3 := sqft_living**3]

test$sqft_living <- as.numeric(test$sqft_living)
test[, power_1 := sqft_living]
test[, power_2 := sqft_living**2]
test[, power_3 := sqft_living**3]

valid$sqft_living <- as.numeric(valid$sqft_living)
valid[, power_1 := sqft_living]
valid[, power_2 := sqft_living**2]
valid[, power_3 := sqft_living**3]

for (i in 4:15) {
  train[, paste('power_', i, sep='') := sqft_living**i]
  valid[, paste('power_', i, sep='') := sqft_living**i]
  test[, paste('power_', i, sep='') := sqft_living**i]
}

model_1 <- lm(price ~ power_1, data = train)
model_2 <- lm(price ~ power_1 + power_2, data = train)
model_3 <- lm(price ~ power_1 + power_2 + power_3, data = train)
model_4 <- lm(price ~ power_1 + power_2 + power_3 + power_4, data = train)
model_5 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5, data = train)
model_6 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6, data = train)
model_7 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7, data = train)
model_8 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8, data = train)
model_9 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9, data = train)
model_10 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10, data = train)
model_11 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10 + power_11, data = train)
model_12 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10 + power_11 + power_12, data = train)
model_13 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10 + power_11 + power_12 + power_13, data = train)
model_14 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10 + power_11 + power_12 + power_13 + power_14, data = train)
model_15 <- lm(price ~ power_1 + power_2 + power_3 + power_4 + power_5 + power_6 + power_7 + power_8 + power_9 + power_10 + power_11 + power_12 + power_13 + power_14 + power_15, data = train)

#for (i in 3:15) {
#  vars <- 'price ~ power_1 + power_2 + power_3'
#  for (j in 1:i) {
#    vars <- paste(vars, ' + power_', j, sep='')
#  }
#  formula <- as.formula(vars)
#  models <- append(models, lm(formula, train))
#}

rss <- function(model, dataset) {
  predictions <- predict(model, dataset)
  residuals <- predictions - dataset$price
  sum(residuals**2)
}

rss_1 <- rss(model_1, valid)
rss_2 <- rss(model_2, valid)
rss_3 <- rss(model_3, valid)

rsss <- c(rss_1, rss_2, rss_3,
          rss(model_4, valid),
          rss(model_5, valid),
          rss(model_6, valid),
          rss(model_7, valid),
          rss(model_8, valid),
          rss(model_9, valid),
          rss(model_10, valid),
          rss(model_11, valid),
          rss(model_12, valid),
          rss(model_13, valid),
          rss(model_14, valid),
          rss(model_15, valid))

min_rss_model <- model_5
rss_of_selected_model_against_test <- rss(min_rss_model, test)
