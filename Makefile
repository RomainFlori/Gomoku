NAME 	=	pbrain-gomoku-ai

RM 		=	@rm -f
PRINT	=	@echo

SOURCES		=	./

$(NAME): ## Generate binary
	@cat shebang $(SOURCES)main.py > $@
	@chmod +x $@
	$(PRINT) "[✔]\tGenerate Binary"

all: $(NAME)

exe: ## Generate binary
	pyinstaller --onefile $(SOURCES)main.py
	@mv ./dist/main $(NAME).exe
	$(PRINT) "[✔]\tBinary (.exe) created"

clean: ## Remove temporary files
	$(PRINT) "[✔]\tRemove pycache"
	$(RM) -r __pycache__ $(SOURCES)__pycache__ $(SOURCES)srcs/__pycache__ $(SOURCES)srcs/commands/__pycache__
	$(PRINT) "[✔]\tRemove temporary files"
	$(RM) -r dist build *.spec

fclean: clean ## Remove binary
	$(PRINT) "[✔]\tRemove binary"
	$(RM) $(NAME)
	$(RM) $(NAME).exe

re: fclean all

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all clean fclean re