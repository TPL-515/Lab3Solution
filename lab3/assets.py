from dagster import asset, get_dagster_logger

##########################################################
################# Insert Code Below ######################
##########################################################

# Get our Logger
logger = get_dagster_logger()

@asset(description="The purpose of this asset is to return crawl and act as a dummy asset for reordering later.")
def crawl(walk):
    # log out information for starting the process
    logger.info('Start the crawl asset')
    return 'crawl'


@asset(description="The purpose of this asset is to return walk and act as a dummy asset for reordering later.")
def walk(run):
    # log out information for starting the process
    logger.info('Start the walk asset')
    return 'walk'

@asset(description="The purpose of this asset is to return run and act as a dummy asset for reordering later.")
def run():
    # log out information for starting the process
    logger.info('Start the run asset')
    return 'run'

@asset(description="The purpose of this asset is to return sprint and act as a dummy asset for reordering later.")
def sprint(walk):
    # log out information for starting the process
    logger.info('Start the sprint asset')
    return 'sprint'


