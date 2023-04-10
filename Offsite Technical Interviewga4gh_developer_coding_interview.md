# Coding Interview [GA4GH Developer]

In this assessment, we would like you to check the compliance of the DRS Starter Kit's *GET /objects/{object_id}* endpoint to the DRS v1.2.0 specification. This can be done by deploying a DRS Starter Kit on your local machine and writing tests to check the compliance of *GET /objects/{object_id}* endpoint.

For this exercise, we are only interested in the *GET /objects/{object_id}* endpoint and the DRS Starter Kit does not enforce any authorization. 

## Background and useful resources:

- **Data Repository Service (DRS) v1.2.0**: https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/
- **GA4GH Starter Kit DRS website:** https://starterkit.ga4gh.org/docs/starter-kit-apis/drs/drs_overview
- **GA4GH Starter Kit DRS Github:** https://github.com/ga4gh/ga4gh-starter-kit-drs

## Requirements of the interview

- You should program in Python3
- If Python is not your main language please flag this in your readme when you submit your solution
- Your code should be of a production level quality written to the best of your ability with Python
- The interview will assess your ability to understand a GA4GH standard, design appropriate methods to test the standard and suggest improvements
- You should indicate on submission back to EBI Recruitment how long you spent on the tasks specified in this exercise

## 1. Deploy a GA4GH Starter Kit DRS on your local machine
 
Follow the instructions in *DRS_Starter_Kit/README.md* file to deploy the DRS Starter Kit and populate it with test DRS objects. You will need to use Docker and Docker Compose

## 2. Write tests to check the following 

Using Python, send a `GET` request to `http://localhost:5000/ga4gh/drs/v1/objects/{object_id}` endpoint with the below listed input DRS object Ids and verify that the outputs are as expected:

|object_id | Expected Status Code | Expected Content Type |
| -------- | -------------------- | --------------------- |
|8e18bfb64168994489bc9e7fda0acd4f  | 200 | JSON |
|ecbb0b5131051c41f1c302287c13495c  | 200 | JSON |
|xx18bfb64168994489bc9e7fda0acd4f  | 404 | JSON |

Your program should provide output to the terminal of the following format:

```
{"object_id" : "8e18bfb64168994489bc9e7fda0acd4f", "test_name" : "NameOfTest", "pass" : true, "message" : "Log message"}
```

You may add additional fields to your JSON output. Each test should emit one line of JSON per test.

## 3. Specify/write additional tests

Please add any other tests that you would carry out to confirm that the "/objects/{object_id}" endpoint follows DRS v1.2 specification. If you are not able to add these tests to your code, please note what you would have tested in your README document.

## 4. How would you package this application?

Please detail in your README how you would approach bundling the application for reuse in another environment e.g. cloud, another desktop machine, alternative operating system

## 5. Submission

Please add your code to a public GitHub repository along with a production quality README document describing your repository, installations, usage and next steps. Email a link to this repository to EBI Recruitment with how long you spent on the tasks in this exercise.
