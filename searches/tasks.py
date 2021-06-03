from haystack import connection_router, connections


def index_object(sender, instance):
    # get possible backends
    backends = connection_router.for_write(instance=instance)

    for backend in backends:
        # get the index for this model
        index = connections[backend].get_unified_index().get_index(sender)
        # update it
        index.update_object(instance, using=backend)
