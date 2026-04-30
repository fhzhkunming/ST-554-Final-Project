# ST-554 Final Project — Spark MLlib & Structured Streaming
This repository contains the final project for ST 554. The project demonstrates how Spark can support both batch machine learning workflows and real time streaming inference within a unified pipeline. The work is organized into two main components:
1.	Building and tuning an Elastic Net regression model using batch data, including SQL based feature engineering, one hot encoding, PCA, and cross validated hyperparameter tuning.
2.	Extending the fitted model to a streaming context, where a python script producing incoming CSV files are processed as micro batches to generate real time predictions and residuals.
Together, these parts show how Spark maintains a consistent transformation workflow across both static and streaming data sources.

**Methods**

**Part 1 — Batch Modeling with Spark MLlib**
- Loaded the power consumption dataset from the UCI Machine Learning Repository.
- Used an SQLTransformer to select relevant variables and prepare the modeling DataFrame.
- Applied one hot encoding to categorical variables.
- Fitted a PCA model to reduce dimensionality.
- Performed cross validated hyperparameter tuning to select the best Elastic Net model.
- Assembled all preprocessing and modeling steps into a complete Spark MLlib transformation pipeline.
- Trained the pipeline on the batch dataset and saved the fitted model for use in streaming.

**Part 2 — Streaming Inference with Structured Streaming**
- Wrote a Python script that continuously generates 20 CSV files, simulating an incoming data stream.
- Created a streaming DataFrame that monitors an input directory (stream_input) for new CSV files using the same schema as the training data.
- Applied the previously fitted pipeline to each micro batch to compute predictions and residuals in real time.
- Printed the resulting output DataFrames to the console as each file arrived.
- Allowed the stream to process all generated files, then stopped the query once streaming was completed.

**Results**
- I successfully transformed the variables required for modeling, fitted a PCA, and performed cross validated hyperparameter tuning using the provided regression and Elastic Net grids. Cross validation selected λ = 0.1 and α = 0.25 as the optimal tuning parameters, with a minimum RMSE of 2147.59. All preprocessing and modeling steps were assembled into a complete Spark MLlib transformation pipeline.
- Using these optimal hyperparameters, the training set RMSE was estimated as 2147.10, and I successfully generated predictions with the fitted Elastic Net model.
- For the streaming component, the Python script generated 20 CSV files in the input directory as expected. The Structured Streaming query ran smoothly and produced 20 output DataFrames in the console, demonstrating that the fitted pipeline can be applied reliably to incoming micro batches.

**Summary**

This project demonstrates an end to end Spark workflow that begins with batch model development and extends seamlessly into real time streaming inference. The first part focuses on building a robust Elastic Net regression model using SQL based feature engineering, one hot encoding, PCA, and cross validated tuning within a Spark MLlib pipeline. The second part shows how this fitted pipeline can be applied directly to streaming data, with Spark Structured Streaming processing incoming CSV files as micro batches and producing real time predictions and residuals.

By integrating these two components, the project highlights Spark’s ability to unify preprocessing, modeling, and streaming inference within a single coherent framework.
