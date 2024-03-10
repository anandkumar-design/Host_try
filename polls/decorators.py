from rest_framework.response import Response
from rest_framework import status

def validate_integers(func):
    def wrapper(request, *args, **kwargs):
        try:
            a = int(request.data.get('a'))
            b = int(request.data.get('b'))
            # If both 'a' and 'b' are integers, proceed with the original function
            return func(request, *args, **kwargs)
        except (TypeError, ValueError):
            return Response({'error': 'Invalid input. Both "a" and "b" must be integers.'}, status=status.HTTP_400_BAD_REQUEST)
    return wrapper