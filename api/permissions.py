from rest_framework  import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # In permissions.SAFE_METHODS there are GET, HEAD, OPTIONS request, if the request method that was passed in this function is one of them, then return TRUE
        if request.method in permissions.SAFE_METHODS:
            return True

        # if its not GET, HEAD or OPTIONS, we need to check if the user requesting is equal to the object's user/owner.
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

