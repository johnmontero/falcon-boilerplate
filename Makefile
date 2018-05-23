.DEFAULT_GOAL := help

TAG = latest
IMAGE_NAME = app
PROYECT_NAME = app
CONTAINER_NAME = app
CONTAINER_OWNER = app

######## Manage containers status (default target = all)
status: ## Show containers status, use me with: make status target=api
	docker-compose ps ${target}

start: ## Up the docker containers, use me with: make up target=api
	docker-compose up -d ${target}

restart: ## Restart the docker containers, use me with: make restart target=api
	docker-compose restart ${target}

stop: ## Stops the docker containers, use me with: make stop target=api
	docker-compose stop ${target}

down: ## Stops and removes the docker containers, use me with: make down target=api
	docker-compose down ${target}

delete: ## Delete the docker containers, use me with: make delete target=api
	docker-compose rm -fv ${target}

build: ## Build the docker containers, use me with: make build target=api
	docker-compose build ${target}

rebuild: ## Rebuild the docker containers, use me with: make rebuild
	make stop
	make delete
	make build
	make start

logs: ## Logss the docker containers, use me with: make logs target=api
	docker-compose logs -f ${target}

ssh: ## SSH connect to container, se me with: make ssh target=api
		docker-compose -p $(PROYECT_NAME) run --rm ${target} sh -c "bash"

######## Manage containers execution
exec: ## Execute command in the docker container, use me with: make exec target=api cmd=ls
	docker exec ${target} ${cmd}

######## Build image from container
commit: ## Commit the docker containers, use me with: make commit target=api revision=1.0
	docker commit ${options} ${target} ${revision}


######## Tag images
tag: ## Tag the docker containers, use me with: make tag.all version=1.0
	docker tag ${CONTAINER_NAME}_api ${CONTAINER_OWNER}/${CONTAINER_NAME}_api:${version}
	
######## Push images
push: ## Push all the docker containers, use me with: make push.all version=1.0
	docker push ${CONTAINER_OWNER}/${CONTAINER_NAME}_api:${version}
	
######## Pull images
pull: # Pull all the docker containers, use me with: make pull.all version=1.0
	docker pull ${CONTAINER_OWNER}/${CONTAINER_NAME}_api:${version}


###### Help
help:
	@echo  'Development commands for project ${PROYECT_NAME}'
	@echo
	@echo 'Usage: make COMMAND [target=some-targets] [cms=some-commads] [revision=some-revision]'
	@echo
	@echo 'Targets:'
	@echo
	@echo '  api            API Rest'
	@echo
	@echo '  default target=all'
	@echo
	@echo 'Commands:'
	@echo
	@grep -E '^[a-zA-Z_-]+.+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo