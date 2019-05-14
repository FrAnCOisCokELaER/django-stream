#!/bin/bash

tag=$(git describe --tags)
buildnumber=
if [ -z "$BUILD_NUMBER" ]
then
    buildnumber="SNAPSHOT"
else
    buildnumber="$BUILD_NUMBER"
fi

tag="${tag}-${buildnumber}"
projectname=$(git remote show origin -n | grep "Fetch URL" | awk -F / '{print $NF}' | awk -F . '{print $1}')

echo "Building images ..."
docker build --build-arg BUILDTIME_APIVERSION=${tag} -t ${projectname} .
echo "Tagging "${projectname}":latest and "${projectname}:${tag} " images" 
docker tag ${projectname} vkh06/${projectname}:latest
docker tag ${projectname} vkh06/${projectname}:${tag}
cat ./docker_credentials.txt | docker login --username=vkh06 --password-stdin
echo "Pushing images to DockerHub"
docker push vkh06/${projectname}:latest
docker push vkh06/${projectname}:${tag}
