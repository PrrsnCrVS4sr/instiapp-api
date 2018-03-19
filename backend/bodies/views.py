"""Views for bodies app."""
from rest_framework import viewsets
from rest_framework.response import Response
from bodies.serializers_followers import BodyFollowersSerializer
from bodies.serializers import BodySerializer
from bodies.serializers import BodySerializerMin
from bodies.models import Body
from roles.helpers import user_has_privilege
from roles.helpers import user_has_insti_privilege
from roles.helpers import forbidden_no_privileges
from roles.helpers import login_required_ajax
from roles.helpers import insti_permission_required

class BodyViewSet(viewsets.ModelViewSet):   # pylint: disable=too-many-ancestors
    """API endpoint that allows bodies to be viewed or edited."""
    queryset = Body.objects.all()
    serializer_class = BodySerializer

    @classmethod
    def list(cls, request): #pylint: disable=unused-argument
        """Override list method"""
        queryset = Body.objects.all()
        serializer = BodySerializerMin(queryset, many=True)
        return Response(serializer.data)

    @insti_permission_required('AddB')
    def create(self, request):
        """Creates body if the user has institute privileges."""
        return super().create(request)

    @login_required_ajax
    def update(self, request, pk):
        """Updates an existing body if the user has privileges."""
        if not user_has_privilege(request.user.profile, pk, 'UpdB'):
            return forbidden_no_privileges()
        return super().update(request, pk)

    @insti_permission_required('DelB')
    def destroy(self, request, pk):
        """Deletes an existing body if the user has privileges."""
        return super().destroy(request, pk)

class BodyFollowersViewSet(viewsets.ModelViewSet):   # pylint: disable=too-many-ancestors
    """API endpoint that lists followers of bodies."""
    queryset = Body.objects.all()
    serializer_class = BodyFollowersSerializer
