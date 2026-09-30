**1. Four reasons a cloud machine beats a laptop for data science at scale**

1. **Scalable resources:** You can rent far more CPU, RAM, GPU and storage than a laptop has, and resize as the job grows.
2. **Always on:** Long-running jobs, scrapers and servers keep running when your laptop is closed or offline.
3. **Accessible and shareable:** Collaborators can reach the same machine, data and services from anywhere, as your friend did with your web server.
4. **Pay for what you use and reproducible:** You can spin up many identical machines for a job, then shut them down, without buying hardware.

**2. Stages of the data science process**

1. **Define the question:** Decide what problem you're trying to answer and what a useful answer looks like.
2. **Collect the data:** Gather the raw data needed, from files, databases, APIs or scraping.
3. **Clean and prepare:** Fix errors, handle missing values, and reshape the data into a usable format.
4. **Explore:** Summarize and visualize the data to understand its patterns, quirks and limits.
5. **Model and analyze:** Apply statistical or machine learning methods to answer the question.
6. **Interpret and communicate:** Explain what the results mean, how reliable they are, and share them with others.

**3. Data analytics vs. data science**

Data analytics focuses on examining existing data to answer specific, usually well-defined questions about what happened and why, mostly through querying, statistics and reporting. Data science is broader: it includes analytics but also involves framing open-ended questions, collecting and engineering new data, and building predictive models or data-driven systems.

**4. Example of a loop in the process**

Suppose you're predicting apartment prices, and during exploration you discover that many listings are missing their neighborhood. That sends you back to the collection stage to scrape the missing field, then back through cleaning before you can continue. Similarly, if your model performs poorly, you might return to redefine the question or gather better features.