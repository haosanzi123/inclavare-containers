#!/bin/bash

PROJECT_DIR=/root/yanrong/yaole/inclavare-containers/warm/ubuntu/
DEBBUILD_DIR=$(mktemp -u /tmp/debbuild.XXXX)
SCRIPT_DIR=$(pwd)
PACKAGE=warm-pal
PROJECT=inclavare-containers
VERSION=0.5.0
TARBALL_NAME=$PACKAGE\_$VERSION.orig.tar.gz
DEB_BUILD_FOLDER=$DEBBUILD_DIR/$PACKAGE-$VERSION

# create and rename the tarball
mkdir -p $DEBBUILD_DIR
cp /root/yanrong/yaole/inclavare-containers/warm/ubuntu/WAMR-09-29-2020.tar.gz $DEBBUILD_DIR
tar zxfP $DEBBUILD_DIR/WAMR-09-29-2020.tar.gz -C $DEBBUILD_DIR
mv $DEBBUILD_DIR/wasm-micro-runtime $DEBBUILD_DIR/$PACKAGE-$VERSION
cd $DEBBUILD_DIR && tar zcfP $TARBALL_NAME $PACKAGE-$VERSION

# build deb package
cp -rf  $SCRIPT_DIR/debian $DEB_BUILD_FOLDER
cd $DEB_BUILD_FOLDER
dpkg-buildpackage -us -uc
cp $DEBBUILD_DIR/*.*deb $PROJECT_DIR
echo $DEBBUILD_DIR
#rm -rf $DEBBUILD_DIR
