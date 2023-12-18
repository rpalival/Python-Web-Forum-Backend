# Group Submission - Team members:

## Nikhil Kumar G - nkumarg@stevens.edu

## Raj Palival - rpalival@stevens.edu

# GitHub Url:

https://github.com/rpalival/Python-Web-Forum-Backend

# Estimate of how many hours you spent on the project

We started the project early and spent around 2 weeks on it approximately working 6 hours each per week. Since we are two of us in the team the combined total number of hours spent on this project are 24 hours approximately.

# Description of how we tested the code

We used the Postman tool to test the APIs.

## Collection : 1. Baseline_Extension

1. We created a Postman collection "Baseline_Extension" and created the following Http Requests in it.
   This is exported as "Baseline_Extension.json" in root.

   1. Create Post1 - for Baseline
   2. Get Post1 - for Baseline
   3. Delete Post1 - for Baseline
   4. Get Post1 Again - for Baseline
   5. Create User1 - for Extension 1: Users and User Keys
   6. Create Post2 with User1 - for Extension 1: Users and User Keys
   7. Delete Post2 of User1 with UserKey - for Extension 1: Users and User Keys
   8. Create Post2 Again with User1 - for Extension 1: Users and User Keys
   9. Edit User1 - for Extension 2: User Profiles
   10. Get User1 - for Extension 2: User Profiles
   11. Get Post2 - for Extension 2: User Profiles
   12. Create Post3 as a reply to Post2 - for Extension 3: Threaded Replies
   13. Get Post3 - for Extension 3: Threaded Replies
   14. Get Post2 - for Extension 3: Threaded Replies
   15. Get All Posts : for date range - for Extension 4: Data and Time based range queries
   16. Create Post4 with User1 - for Extension 5: User Based range queries
   17. Get All Posts : for user_id - for Extension 5: User Based range queries

2. We created an environment file called "Web_Forumn" and used it in our Http requests. This is exported as "Web_Forumn.json" in root.
   We created different variables in the environment file for the above Http Requests. So that we can set the response of a particular request to an environment variable and use that environment variable for other requests.

3. We wrote the tests in the 'Tests' section of each Http request in the Postman tool. These tests are described in detail for all the requests in a later section.

4. We installed the command line tester 'newman' and used 'newman run' with "Baseline_Extension.json" and "Web_Forum.json" to test all tests written in the 'Tests' section of the Http Requests.

# Any bugs or issues you could not resolve

There are no bugs in the program.

# An example of a difficult issue or bug and how you resolved it

We got stuck on multiple things here and there but the most painful one was when we were trying to create a post with userid, we were sending the userid as a string but were expecting an integer on the backend in the create post endpoint. There were two solutions to this problem: 1. to type cast the userid into (int) on the backend or 2. Just send an integer to the backend. Because python uses 'dynamic typing' the error took longer to detect and resolve but we reslolved it by pair programming with each other.

# A list of the five extensions you’ve chosen to implement, be sure to describe the endpoints you’ve added to support this, using a documentation format similar to ours.

The five extensions we chose are listed below and they are numbered the same way throughout the project:

1. Extension 1: Users and User Keys
2. Extension 2: User Profiles
3. Extension 3: Threaded Replies
4. Extension 4: Data and Time based range queries
5. Extension 5: User Based range queries

Lets dive deep into each extension:

1.  Extension 1: Users and User Keys

    Endpoints:

    1. Created Endpoint: POST /user

    This endpoint allows you to create a new user. The request should be sent as an HTTP POST to the specified URL. The request body should be in raw format and include the "username" and "real_name" fields.

    Sample body:

    {
    "username": "johndoe69",
    "real_name": "John Doe"
    }

    Sample response: JSON Object with key (i.e., user's key) and user_id

    {
    "key": "\_9z97HfMtzFNPn37hBDmmA",
    "user_id": 1
    }

    2. Modified Endpoint: Post /post

    This endpoint can now create posts with users associated with them. In the body along with the string valued field 'msg', add fields 1. user_key and 2. user_id.

    Sample body:

    {
    "msg": "Hello, World!",
    "user_key": "{{user1secretKey}}",
    "user_id": {{user1_id}}
    }

    Sample Response: JSON returns posts' info

    {
    "id": 1,
    "key": "QGZ3ZfLt60uDdwUO6vfsVA",
    "timestamp": "2023-12-18T03:35:33.741230"
    }

    3. Modified Endpoint: Get /post/<int:id>

    This endpoint gets a post.
    This endpoint will now return the user information as well along with post.
    The endpoint takes post's id as parameter and returns posts' info along with user's info (user_id and username).

    Sample Response:
    {
    "id": 1,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T03:35:33.741230",
    "user_id": 1,
    "username": "johndoe69"
    }

    4. Modified Endpoint: Delete /post/<int:post_id>/delete/<key>

    This endpoint will either take user_key or post_key as key and post_id to delete a particular post.

2.  Extension 2: User Profiles

    Endpoints:

    1. Created Endpoint: GET /user/<identifier>

    This endpoint makes an HTTP GET request to retrieve user information based on the provided user ID. The user ID is passed as a path parameter in the URL.
    The response to the request returns the user's real name, user ID, and username in a JSON format.

    Example:

    GET http://127.0.0.1:5000/user/

    Sample Response:

    {
    "real_name": "",
    "user_id": 0,
    "username": ""
    }

    2. Notice Endpoint: POST /user

    This endpoint creates a new user.
    This endpoint's body takes a 1. unique part: username 2. non-unique part: real name

    Sample body:

    {
    "username": "johndoe69",
    "real_name": "John Doe"
    }

    Sample response: JSON Object with key (i.e., user's key) and user_id

    {
    "key": "\_9z97HfMtzFNPn37hBDmmA",
    "user_id": 1
    }

    3. Created Endpoint: PUT /user/<int:user_id>

    This endpoint allows updating user information using an HTTP PUT request using the user's user_id and key

    Sample Request:
    key: (string) The user's key
    real_name: (string) The user's real name

    Sample Response:
    A success response will have a status code of 200 and a JSON object with a msg field as below:

         {
         "msg": "User metadata updated"
         }

    4. Modified Endpoint: GET /post/<int:id>

    This endpoint gets a post.
    This endpoint will now return the post with user's unique metadate: username by giving post_id in url.

    Sample Response:
    {
    "id": 3,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T04:08:01.993390",
    "user_id": 1,
    "username": "johndoe69"
    }

3.  Extension 3: Threaded Replies

    Endpoints:

    1. Modified Endpoint: POST /post

    This endpoint creates a new post. With this extension this endpoint can now create a post as a reply to another post.

    Just in the request body include field : replying_to_id
    This field takes a post_id as its value. This new post will be a repoly to the post whose id is mentioned here.

    Sample Request: This post is created as a reply to post with id 2.
    {
    "msg": "Hello, World!",
    "replying_to_id": 2
    }

    Sample Response: A new post with id '4' is created.
    {
    "id": 4,
    "key": "6sRCEDHfy3NRb3IwQ5zX7w",
    "timestamp": "2023-12-18T04:30:43.483238"
    }

    2. Modified Endpoint: Get /post/<int:id>

    This is an endpoint to get a post using its id. Now with this extension it will return two extra fields:

    1. replying_to_id - the id of the post it is replying to.
    2. ids_of_replies - ids of all the posts that it has as its replies

    {
    "id": 4,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": 3,
    "timestamp": "2023-12-18T04:30:43.483238",
    "user_id": null,
    "username": null
    }

4.  Extension 4 : Data and Time based range queries

    Endpoint:

    1. Created Endpoint: Get /posts/range?start=timestamp1&end=timestamp2

    This endpoint is used to get all the posts within the specified date range. It has two query parameters that takes start and end date:

    1. start
    2. end

    Example Get request:

    http://127.0.0.1:5000/posts/range?start={{post1_timestamp}}&end={{post2_timestamp}}

    Example Response: It returns a list of all the posts within that date range. If the parameters are not given then it returns all the posts by default.

    [
    {
    "id": 1,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T03:35:33.741230",
    "user_id": 1,
    "username": "johndoe69"
    },
    {
    "id": 2,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T04:07:50.820516",
    "user_id": 1,
    "username": "johndoe69"
    },
    {
    "id": 3,
    "ids_of_replies": [
    4
    ],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T04:08:01.993390",
    "user_id": 1,
    "username": "johndoe69"
    }
    ]

5.  Extension 5: User Based range queries

    Endpoints:

    1. Created Endpoint: Get /posts/user/<int:user_id>

    This endpoint is used to get all the posts for a specific user using their user_id.

    Sample Request:
    http://127.0.0.1:5000/posts/user/{{user1_id}}

    Sample Response: It returns a list of all the posts that belong to user1:

    [
    {
    "id": 1,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T03:35:33.741230",
    "user_id": 1,
    "username": "johndoe69"
    },
    {
    "id": 2,
    "ids_of_replies": [],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T04:07:50.820516",
    "user_id": 1,
    "username": "johndoe69"
    },
    {
    "id": 3,
    "ids_of_replies": [
    4
    ],
    "msg": "Hello, World!",
    "replying_to_id": null,
    "timestamp": "2023-12-18T04:08:01.993390",
    "user_id": 1,
    "username": "johndoe69"
    }
    ]

# Detailed summaries of your tests for each of your extensions, i.e., how to interpret your testing framework and the tests you’ve written

Summary:
Our testing approach for the Flask application using Postman is a comprehensive and dynamic method that effectively leverages Postman’s features like environment variables, request chaining, and detailed assertions to validate the application's functionality.

1. Environment Variables and Request Chaining:
   we’ve skillfully utilized Postman environment variables to store and share data across different requests. This technique is crucial for maintaining context between test runs, especially in scenarios where the output of one request (like the creation of a user or post) is used as input for subsequent requests (such as retrieving or deleting a post). By dynamically setting environment variables like user_id, post_id, and timestamp from the responses of POST requests, you've created a seamless chain of tests that mimic real-world user interactions with the API.
2. JSON Body and Response Validation:
   For POST requests, we’ve meticulously ensured that the JSON bodies contain specific variables and values, adhering to the expected request format of the API. This level of detail guarantees that the requests are not only syntactically correct but also semantically aligned with the application's requirements.
3. Comprehensive Testing:
   Our tests encompass a wide range of assertions - from verifying response status codes and content types to validating the format and integrity of data fields like id, timestamp, key, and username. These tests confirm not only the successful operation of the API endpoints but also the correctness and consistency of the data being returned or modified.
4. Security and Data Integrity Checks:
   we’ve included tests to ensure that sensitive information, like user keys, is not exposed in responses, aligning with best practices in API security. Additionally, by validating data formats and relationships (e.g., post reply structures), your tests reinforce the data integrity of the application.
   In summary, your testing strategy using Postman is a well-thought-out blend of dynamic data handling, precise request formatting, and rigorous validation checks. This strategy ensures thorough coverage of the application’s functionality, from user and post management to intricate features like threaded replies and time-based data retrieval.

Extension 1 - Creating a User:
The tests designed for creating a user involve checking the response after a POST request to the /user endpoint. The following aspects are verified:

- Status Code Verification: The tests ensure that upon successful creation of a user, the status code returned is 200. This is the first line of assurance that the user creation process is working as intended and that the server has understood and processed the request.
- Content-Type Verification: By checking that the Content-Type header is application/json, the tests confirm that the response is in the correct format, which is essential for any client application consuming this API to parse the response correctly.
- Field Existence: The tests check for the presence of key and user_id in the response, which are essential pieces of data for user identification and authentication in future interactions with the API.
- Data Type Checks: The user_id is tested to be a non-negative integer, ensuring the integrity of the user identifier. The key is verified to be a base64 URL-safe string, aligning with security standards for randomness and URL compatibility.

Extension 2 - Modifying a User:
For modifying user metadata, the tests target the PUT request to the /user/<int:user_id> endpoint and perform the following verifications:

- Successful Update Confirmation: Similar to user creation, a status code of 200 indicates a successful update operation. The response message 'User metadata updated' further asserts that the intended change has been made.
- Content-Type Verification: Ensuring that the response is application/json.
- Field Verification: Here, the test checks whether the msg field exists and contains the correct confirmation message, which is crucial for feedback in client applications.

Extension 3 - Threaded replies:
Here's how the functionality of Extension 3 is tested:

- Status Code Verification: Initially, tests confirm that the server responds with a 200 OK status code after a post creation attempt. This indicates the request was successfully received, understood, and processed.
- Data Integrity Checks: The tests validate that the id of the newly created post is a non-negative integer, ensuring a valid and unique identifier is assigned to each post. Additionally, the key is verified to be a proper base64 URL-safe string, which is critical for the secure identification and later manipulation (like deletion) of the post.
- Timestamp Validation: The validity of the timestamp is checked against the ISO 8601 format, ensuring that the date and time of the post creation are recorded in a standard and consistent manner.
- Content-Type Assertion: By asserting that the Content-Type header is application/json, the tests ensure that the response is in JSON format, which is the expected content type for RESTful APIs.
- Response Structure Verification: The tests examine the response body to verify the presence of required fields, such as id, key, and timestamp. The presence of these fields in the correct format is indicative of a well-formed response.
- Reply Linkage Confirmation: For posts created as replies, the tests verify that the replying_to_id field matches the expected id of the original post to which the reply is directed. This linkage is crucial for maintaining the thread integrity in a conversation.
- Ids of Replies Array: The tests ensure that the ids_of_replies field exists and is an array. This is significant as it should contain the ids of all posts replying to the current one, thus confirming that the thread hierarchy is maintained.
- Username Association: When a user creates a post, their username should be associated with the post. The tests check for the existence and correctness of the username in the post details, ensuring that replies are correctly attributed to their authors.
- Environment Variables Utilization: By setting environment variables with details of the created posts (like post3_id and post3_timestamp), the tests can use these variables to reference posts in subsequent requests. This allows for dynamic testing within the same execution flow and ensures that related requests are appropriately chained, which is particularly important for testing reply functionality.
- Comprehensive Response Matching: Finally, the tests compare the entire response body to the expected values set in the environment variables. This comprehensive match includes checking the id, timestamp, msg, user_id, and any ids_of_replies. If the post is a reply, the replying_to_id is also checked to ensure it matches the id of the original post. This end-to-end validation confirms that all aspects of the post creation process are functioning as intended.

Extension 4 - Date and time-based range queries:
Testing Extension 4, which involves retrieving all posts within a specified date and time range. This feature allows users to filter posts based on their creation times, enhancing the user experience by providing a focused view of the content. The Postman tests written for this extension rigorously assess its functionality.
Overview of Tests:

- Status Code Verification: The first test ensures the server responds with a 200 OK status code when the /posts/range endpoint is accessed. This confirms the server successfully processes the request and the date range query parameters are valid and understood.
- Content-Type Validation: The second test checks the response header for application/json, verifying that the response data is in JSON format. This consistency in response format is crucial for any client applications consuming the API, as it ensures the data can be easily parsed and used.
- Response Structure and Data Integrity:
  - Array Structure: The tests verify that the response is an array of objects, each representing a post. This is essential since the endpoint is expected to return multiple posts.
  - Ids of Replies: It's confirmed that the ids_of_replies field within each post object is an array. This check is vital for maintaining the thread integrity of replies in the forum.
  - Timestamp Format: The timestamp of each post is validated against the ISO 8601 format. This ensures that the time data is standardized and accurately represents when each post was created.
- Matching Response Data with Environment Variables:
  - The test suite includes assertions to match specific fields like id, timestamp, user_id, username, and replying_to_id against expected values stored in Postman environment variables. This dynamic testing approach is crucial for validating that the API returns the correct data based on the query parameters.
  - Notably, the tests check whether the returned posts fall within the requested date and time range. By setting and retrieving environment variables for expected values, the tests can dynamically validate the correctness of the data returned by the API.
- Key Absence Verification: The tests ensure that sensitive information like the key is not included in the response, adhering to security best practices by not exposing potentially sensitive data.
- Comprehensive Validation: The tests cover all critical aspects of the response – structure, data types, and values – ensuring a thorough validation of the endpoint's functionality.

Extension 5 - User-based range queries (needs user):
Testing Extension 5, which involves retrieving all posts created by a specific user. This feature enables users to view all contributions made by a particular user.
Overview of the Testing Approach:

- Response Status and Content Verification:
  - Status Code: The tests begin by verifying that the server responds with a 200 OK status, indicating a successful retrieval of posts for the specified user.
  - Content-Type: Ensuring the response header includes application/json validates that the data is returned in a universally accepted format, facilitating ease of parsing and integration in various client applications.
- Response Structure Assessment:
  - The tests inspect the structure of the JSON response. The response is a List of all posts, hence the tests focus on individual posts within this array (firstPost, secondPost, etc.).
  - For each post, the tests check the existence and array nature of ids_of_replies, affirming that the response correctly includes information about any replies to the post.
- Data Integrity and Format Checks:
  - Timestamp Validation: Each post’s timestamp is validated against the ISO 8601 standard, ensuring the date and time data are accurately represented.
  - Post Attributes: The tests confirm the presence of key fields (id, timestamp, msg, user_id, username, replying_to_id) and verify their data types and values.
  - Key Absence: The tests ensure sensitive data like the key is not included in the response, adhering to privacy and security best practices.
- Dynamic Validation with Environment Variables:
  - By setting and using environment variables like post2_id, post2_timestamp, and user1_id, the tests can dynamically compare the response data against expected values. This is crucial for testing scenarios with varying data.
- Comprehensive Data Matching:
  - The tests rigorously compare the response data against expected values. For instance, verifying if the id in the response matches the post2_id environment variable confirms that the API is returning the correct post.
  - Similarly, comparing other fields like timestamp, user_id, msg, and username ensures that each post in the response is correctly attributed to the user in question and contains accurate information.
- Reply Linkage and User Attribution:
  - For posts that are replies, the tests verify the replying_to_id field to ensure it correctly references the original post.
  - The username associated with each post is checked to ensure that the posts are correctly attributed to the user whose posts are being queried.
