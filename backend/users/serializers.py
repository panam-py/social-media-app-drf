from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message='There is already another user with this email address')])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="Username already in use")])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('date_joined', 'is_active', 'last_login', 'groups', 'user_permissions', 'profile_pic', 'is_superuser', 'reactions')
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            }
        }

    
    def validate(self, attrs):
        password, confirm_password = attrs['password'], attrs['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(detail="Passwords do not match", code=400)

        return super().validate(attrs)

    
    def create(self, validated_data):
        email, first_name, last_name = validated_data['email'], validated_data['first_name'], validated_data['last_name']
        password, username = validated_data['password'], validated_data['username']

        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, reactions=[''], username=username)
        user.save()
        return user


