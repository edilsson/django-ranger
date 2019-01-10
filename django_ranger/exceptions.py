class ParameterError(BaseException):
    """
    used in UserGrant or GroupGrant model when it tries to save instances
    with inconsistent parameter_values and permission.parameters_definition
    """
    pass


class DoesNotExist(BaseException):
    """
    used in PermissionManager when user has no grant added.
    """
    pass
