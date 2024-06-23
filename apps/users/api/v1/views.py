from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.users.models import CustomUserModel
from apps.users.api.v1.serializers import CustomUserSerializer
from apps.utils.generics.permissions import IsManager, IsCustomer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing CustomUserModel instances.
    """

    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """
        Get the list of permissions that the current action requires.

        Returns:
            list: A list of permission classes.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = [IsManager]
        else:
            self.permission_classes = [IsCustomer | IsManager]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """
        This method overrides the default create method to include the `authentication_token` in the response
        if the user is created successfully.

        Returns:
            Response: The response containing a success message and the `authentication_token`.
        """
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = CustomUserModel.objects.get(username=response.data['username'])
            data = {'message': 'Created successfully', 'authentication_token': user.authentication_token}
            return Response(data, status.HTTP_201_CREATED)
        return response

    def update(self, request, *args, **kwargs):
        """
        Update a CustomUserModel instance. This method overrides the default update method to return a custom success message.

        Returns:
            Response: The response containing a success message.
        """
        super().update(request, *args, **kwargs)
        return Response({'message': "Updated successfully"})

    def destroy(self, request, *args, **kwargs):
        """
        Delete a CustomUserModel instance. This method overrides the default destroy method to return a custom success message.

        Returns:
            Response: The response containing a success message.
        """
        super().destroy(request, *args, **kwargs)
        return Response({'message': "Deleted successfully"}, status.HTTP_204_NO_CONTENT)
