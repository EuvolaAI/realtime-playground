SERVER := realtime-agent
cur_dateTime := $(shell date +'%Y%m%d%H%M')
image_address := hkccr.ccs.tencentyun.com/aibum/${SERVER}:test_${cur_dateTime}
image_address_latest := hkccr.ccs.tencentyun.com/aibum/${SERVER}:latest
image_address_aws :=  584754022186.dkr.ecr.us-east-1.amazonaws.com/aibum/${SERVER}:${cur_dateTime}
image_address_aws_latest :=  584754022186.dkr.ecr.us-east-1.amazonaws.com/aibum/${SERVER}:latest
WEB_DIR = ./web
PNPM = pnpm

upload: build
	docker build --platform linux/amd64 -t ${image_address} -t ${image_address_latest} . --push

uploadaws: build
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 584754022186.dkr.ecr.us-east-1.amazonaws.com
	docker build --platform linux/arm64 -t ${image_address_aws} -t ${image_address_aws_latest} . --push

build:
	echo "Building web project"
# 	cd $(WEB_DIR) && rm -rf .next node_modules
	cd $(WEB_DIR) && $(PNPM) install && $(PNPM) build