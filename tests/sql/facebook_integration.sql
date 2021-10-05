create table facebook_integration (
    id bigserial,
    ad_object_id text,
    access_token text,
    created_at timestamptz
);

insert into facebook_integration(ad_object_id, access_token, created_at) values
('act_283849375686242', 'EAAhMVyE1D1kBAJ0ZAFoQeLlOagmj6ZA8VdeKKgfvuvsBU9s8fMSnXU1s7km9WxZCuYBqchZCHed8FOZAQlH1sSmAK6fWhwlQeiMQwXxRtde0luzjixV9sH9fVNzhN7VHUFcroIULHABsSaqDmE5ZCShK0JmPmlNC6AuzuHfmasuYn9ZBC62vZBMc', '2020-03-02 19:34:55.636086+00'),
('act_1091729964179213', 'EAAhMVyE1D1kBAAYluIkp9avRErLtlJnL6hjS38ney2LqOJMyVaG9NlJYgObRaX089Oh0pS4HuZAm7rP1AxIbefpDChpEBuu72G8hgGs9tURYNPLbWoiVUEbjjpunS5XsPbSmEFiH2gZCeglQZCykFZCykv5u1xhe4y0QFB3D34vrYbAKrEze', '2020-03-20 18:08:25.310496+00'),
('act_283849375686242', 'EAAhMVyE1D1kBANBgEkTJP6P6ZAaZBxeLMwBl8SwVpVf2NxvFy3swNzQ3Ozv326Q3DojxIzzJRSF9G5cOqZAaLUS3ndhyWI8hQHCs3HZBm9EZAZAbfKhHrOAqox8izgZBCbJdRG0SRWPcIwZCAH0RjTDqVZCuEHZBnZBFyKmZBB2PZBGzbZANf2xTZB4L5Hs', '2020-02-29 00:54:30.895981+00'),
('act_319883982', 'EAAhMVyE1D1kBAJ0Srt8eXc6gILqS8Ts7Cvwgms8HoZAjiuUQeM6hDFBtwdzFyiIEK6hSs1ZCsvbhyELTSm0olJRdgyS2TsbGOLVficDlYaBX8IKRY4OTiDzAlrQE5vfhVnnyqMhn6Fm4nq8M2DNlfW0UPEmzAUfA0ZAbboMLAZDZD', '2020-05-14 14:15:13.823899+00'),
('act_2141141252878085', 'EAAhMVyE1D1kBANKNtblD5avuKaelTsnJCf3dew1F9ihS8ar7bfZB8zbNqlwywa3wHtC0wvClA1oAb6swIzWz9pP3vr1qOWFGuZBSs6jRZCU8z5ndqCYLbofnAEV4jncZBSkGHxgsnJ84W2fahYZAcj4z0Cl6DFceYIRZBC9ZCRQDgZDZD', '2020-02-29 12:17:25.558041+00'),
('act_283849375686242', 'EAAhMVyE1D1kBANQaHvH5cbouX1E8IZCFuVvV0fv8epy2o9RZBrzrTpLo2tSOT4qZA9nH2ZChUQmqNjUZCw9lHEyihL27dXsPZC8TtAMqC6h8h0K2SX0NnvrIeI7xSSVgOyJUjZBmrJPeZBkVWKyCvZBCgLznCQBA9kkZCXJcRdgij7XzWRmE6lf48L', '2020-08-26 18:37:20.424603+00'),
('act_283849375686242', 'EAAhMVyE1D1kBAOZBlvqHu0gEl0cIXxKi6wy3OdU5E4QkZA7LWWIUa3feIXoBkTPEuApUHOaJZCgEeJ48dKcnI7EsAqcyw0pwsRHVkFuJbHb4PqMzXx88tZB6AFGLN0p9rzCpz3t7qCSFS2dpfXDMY9djRakYWzM6lWpZAb7r9zdgSOYdnq21a', '2020-08-27 16:30:23.19098+00'),
('act_283849375686242', 'EAAhMVyE1D1kBAGe8OfFZBuVOVgw46VZC8wUEr7y60kNUGQ1Q3mjEb8p2AlZCb5GL8qLzELwCPHFEZBGSyjVpBrtziA4ZCgdjuB0yGiKQjx8zqXoR7ZChrNSFzN5wr9PJGXZCJ4MOp4dasKF3boRme62Oa0fqjiWlSpZBT8RbrUQyBnYb8yYg9cMJ', '2021-05-01 12:05:55.335241+00'),
('act_41905985', 'EAAhMVyE1D1kBAKmyfvMPJal31clOuzSo6ngZBdUxYnlP4M281lxHAiYeOZBleDygvAuMdoWvLLVjJS3gxCkhj1LOFSwCgU6FEa96Xvc6C8ZCoeI0zv2w4cIKfeZAPLlaO7BGstxpZComSQwlpcVp41CgguBRkapbwhutborPmA9evRBm0Y3b0sb3Qk89uh18ZD', '2021-01-06 22:01:16.849945+00'),
('act_319883982', 'EAAhMVyE1D1kBAOVnBJadfloQJiuVZAzfzHE4jnYfMbKYNBrH1Iu3OZBXWfXsIZAtI1fVZAYCwqyOoxQpDKkcW0jdULTZAyGbH3fu5oUaMs7i6PXoo0yEiEo9G3e1QaRTEDCZBrLkxMqpC7tFmXE364M1jzV4KgwOKQWpOqcb4YCNaacwhJxs9a', '2021-04-29 23:58:05.984993+00');