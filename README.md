# drivers-test-availability-check

> A basic program written in Python using Selenium to automatically navigate through the steps in the Minnesota drivers test scheduling site.

## Why?

I got tired of putting in the same information over and over to find nothing. So, I made this program where I could run it and quickly check availability saving me a couple of minutes of my day.

## Configuration

Change the `permitNumber` and `BDay` variables to your own Permit Number and Birthday. Lastly, get the latest driver for your browser of choice and place it in the same directory as the `drivers_test.py`. To find the proper driver for your browser check [here](https://selenium-python.readthedocs.io/installation.html#drivers).

## How to run?

It's as simple as installing selenium via `pip install selenium`, configuring it for your browser (see configuration) and running the `drivers_test.py`.

## I need "X" fixed

Well, I can't help you much. Once you book an appointment or pass you driving test you can't use your permit number or license number to look for appointments. I've now passed my driver's test and am just releasing this code for people to build upon and/or fix.

> Date: 8/1/2024
