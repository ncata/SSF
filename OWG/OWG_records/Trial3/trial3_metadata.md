OWG Notes:
Trial 3:
  Time: 2017, 70 % of data, 30% held for independent validation
  Wall time: 1 hour 7 minutes 51 seconds.
  Batch size: 8
  Resolution: 512x512
  Number of images: 355
  mse loss: 0.0352m
  mae: 0.1528m
  R 2 value: .90571
  MAPE: 25.880342910952486
  Notes:
    Third trial using GLERL imagery.
     All images with intensity scores under 85 were thrown out as many night images had snuck in due to the harbor lights
     Images that had a sharpness score below 3.5 were removed.
     Batch size r=was reduced to 13 to get past a ResourceExhaustedError and to follow Dan Buscombe's recommendations for testing new hyper-parameters as the project moves forward.

  Application:
    Number of images: 245
    R 2 value: 0.65203
    MAPE: 52.60329987677864
    Notes:
      Application of model is still seriously underperforming. Leading hypothesis for this is over training as increased quality control did not close the gap.
