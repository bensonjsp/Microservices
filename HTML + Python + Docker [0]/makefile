PROJECT_NAME = "hotel-room"
LOCAL_DEPLOY_DIR = "./"

up: # Rebuild image(s), if changes made. Run containers from rebuilt image(s). remove-orphans to remove containers no longer in use
	@docker compose -p ${PROJECT_NAME} \
		-f ${LOCAL_DEPLOY_DIR}/compose.yaml \
		up --build -d --remove-orphans

down: # Bring down containers. Remove dangling (not attached to anything) images, networks, containers, and volumes.
	@docker compose -p ${PROJECT_NAME} \
		-f ${LOCAL_DEPLOY_DIR}/compose.yaml \
		down
	@docker system prune -f --volumes

down-clean: # Remove EVERYTHING
	@docker compose -p ${PROJECT_NAME} \
		-f ${LOCAL_DEPLOY_DIR}/compose.yaml \
		down --remove-orphans
	@docker system prune -f -a