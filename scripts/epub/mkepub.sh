#!/bin/bash
docker build -f scripts/epub/Dockerfile -t sfosc-epub .
id=$(docker create sfosc-epub)
docker cp $id:/dist/sfosc.epub - > sfosc.epub
docker rm -v $id
