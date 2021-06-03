from haystack import connection_router, connections


def handle_save(self, sender, instance, **kwargs):
    # get possible backends
    backends = self.connection_router.for_write(instance=instance)

    for backend in backends:
        # get the index for this model
        index = self.connections[backend].get_unified_index().get_index(sender)
        # update it
        index.update_object(instance, using=backend)


def handle_delete(self, sender, instance, **kwargs):
    """
    Given an individual model instance, determine which backends the
    delete should be sent to & delete the object on those backends.
    """
    backends = self.connection_router.for_write(instance=instance)

    for using in backends:
        try:
            index = self.connections[using].get_unified_index().get_index(sender)
            index.remove_object(instance, using=using)
        except Exception:
            # TODO: Maybe log it or let the exception bubble?
            pass
