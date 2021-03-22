from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
	rud 		=		serializers.HyperlinkedIdentityField(view_name="activity:RUD",lookup_field="id")
	class Meta:
		model 	=	Activity
		fields 	=	"__all__"