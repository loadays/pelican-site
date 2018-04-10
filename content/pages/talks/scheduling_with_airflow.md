## Scheduling data pipelines (Bert Desmet) ##

The back-end of big analytical projects are often split in multiple small tasks. 
Most 'enterprise' tools include their own scheduler, but if you want to combine your ETL flow with your spark jobs with specific python or R scripts, a more specialized scheduler will be needed. 
In this session I will explain multiple scheduling concepts (DAG, triggers, Branching, parameters and ‘batching’) with Airflow, AirBNB’s own scheduling solutions.