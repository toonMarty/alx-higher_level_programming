#!/usr/bin/node
async function getStatusCode () {
  const requestURL = process.argv[2];
  const request = new Request(requestURL);
  const response = await fetch(request);
  const statusCode = response.status;

  console.log('code: ', statusCode);
}

getStatusCode();
