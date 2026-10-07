# Entry point for development: draws the chart and runs the tests.
import sea_level_predictor
from unittest import main

# Draw and save the chart
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)
