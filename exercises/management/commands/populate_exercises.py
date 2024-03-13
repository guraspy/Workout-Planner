from django.core.management.base import BaseCommand
from exercises.models import Exercise

class Command(BaseCommand):
    help = 'Populate the database with 20 predefined exercises'

    def handle(self, *args, **kwargs):
        exercises = [
            {
                'name': 'Push-up',
                'description': 'A classic bodyweight exercise targeting the chest, shoulders, and triceps.',
                'instructions': '1. Start in a plank position. 2. Lower your body until your chest nearly touches the floor. 3. Push back up to the starting position.',
                'target_muscles': 'Chest, Shoulders, Triceps',
                'repetitions': 10,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Squat',
                'description': 'A compound exercise targeting the quadriceps, hamstrings, glutes, and core muscles.',
                'instructions': '1. Stand with feet shoulder-width apart. 2. Lower your body as if sitting back into a chair. 3. Keep chest up and back straight. 4. Push through heels to return to standing position.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes, Core',
                'repetitions': 12,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Pull-up',
                'description': 'A challenging bodyweight exercise targeting the back, biceps, and shoulders.',
                'instructions': '1. Hang from a pull-up bar with palms facing away. 2. Pull your body up until chin clears the bar. 3. Lower back down with control.',
                'target_muscles': 'Back, Biceps, Shoulders',
                'repetitions': 8,
                'sets': 4,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Deadlift',
                'description': 'A compound exercise targeting the posterior chain, including the lower back, glutes, and hamstrings.',
                'instructions': '1. Stand with feet hip-width apart, barbell in front of you. 2. Hinge at the hips, keeping back straight, to grip the bar. 3. Lift the bar by extending hips and knees, keeping it close to body. 4. Lower with control.',
                'target_muscles': 'Lower Back, Glutes, Hamstrings',
                'repetitions': 8,
                'sets': 4,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Bench Press',
                'description': 'A classic chest exercise using a barbell or dumbbells.',
                'instructions': '1. Lie on a bench, feet flat on the floor. 2. Grip the barbell with hands shoulder-width apart. 3. Lower bar to chest, keeping elbows at 45-degree angle. 4. Press bar back up to starting position.',
                'target_muscles': 'Chest, Shoulders, Triceps',
                'repetitions': 10,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Lunges',
                'description': 'A leg-strengthening exercise targeting the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Stand with feet hip-width apart. 2. Step forward with right leg, lowering body until both knees are at 90-degree angle. 3. Push back up to starting position. 4. Repeat on other side.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes',
                'repetitions': 12,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Dumbbell Shoulder Press',
                'description': 'An overhead pressing exercise targeting the shoulders and triceps.',
                'instructions': '1. Sit on a bench, holding dumbbells at shoulder height. 2. Press dumbbells overhead until arms are fully extended. 3. Lower back down with control.',
                'target_muscles': 'Shoulders, Triceps',
                'repetitions': 10,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Russian Twist',
                'description': 'A core exercise that targets the obliques and abdominal muscles.',
                'instructions': '1. Sit on the floor, knees bent and feet elevated. 2. Hold a weight or medicine ball. 3. Twist torso to the right, touching weight to floor. 4. Twist to the left and repeat.',
                'target_muscles': 'Obliques, Abdominals',
                'repetitions': 20,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Mountain Climbers',
                'description': 'A dynamic exercise that engages the core, shoulders, and legs.',
                'instructions': '1. Start in a push-up position. 2. Bring right knee towards chest, then quickly switch legs. 3. Continue alternating legs at a rapid pace.',
                'target_muscles': 'Core, Shoulders, Legs',
                'repetitions': 30,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Burpees',
                'description': 'A full-body exercise that combines a squat, push-up, and jump.',
                'instructions': '1. Start in a standing position. 2. Drop into a squat, placing hands on floor. 3. Jump feet back into a push-up position. 4. Perform a push-up, then jump feet back to hands. 5. Explosively jump up, reaching arms overhead.',
                'target_muscles': 'Full Body',
                'repetitions': 10,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Leg Press',
                'description': 'A machine exercise targeting the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Sit on leg press machine with feet on platform. 2. Press platform away from body by extending knees. 3. Lower platform back to starting position with control.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes',
                'repetitions': 12,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Tricep Dips',
                'description': 'An exercise targeting the triceps, shoulders, and chest.',
                'instructions': '1. Sit on a bench or chair with hands beside hips, fingers forward. 2. Lift hips off bench and walk feet forward. 3. Lower body by bending elbows to 90 degrees. 4. Push back up to starting position.',
                'target_muscles': 'Triceps, Shoulders, Chest',
                'repetitions': 12,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Bicycle Crunches',
                'description': 'A core exercise that targets the rectus abdominis and obliques.',
                'instructions': '1. Lie on back, hands behind head, legs lifted and knees bent. 2. Bring right elbow towards left knee while extending right leg. 3. Switch sides, bringing left elbow towards right knee.',
                'target_muscles': 'Rectus Abdominis, Obliques',
                'repetitions': 20,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Barbell Bent Over Row',
                'description': 'A back-strengthening exercise that targets the lats, rhomboids, and biceps.',
                'instructions': '1. Bend at hips with knees slightly bent, holding barbell with overhand grip. 2. Pull barbell towards lower chest, keeping elbows close to body. 3. Lower back down with control.',
                'target_muscles': 'Lats, Rhomboids, Biceps',
                'repetitions': 10,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Seated Leg Curl',
                'description': 'A machine exercise targeting the hamstrings.',
                'instructions': '1. Sit on leg curl machine with legs under pad. 2. Curl legs towards glutes by flexing knees. 3. Lower back down with control.',
                'target_muscles': 'Hamstrings',
                'repetitions': 12,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Calf Raises',
                'description': 'An exercise to strengthen the calf muscles.',
                'instructions': '1. Stand on edge of step or platform with heels hanging off. 2. Rise up onto toes, then lower heels below platform. 3. Repeat.',
                'target_muscles': 'Calves',
                'repetitions': 15,
                'sets': 3,
                'duration_minutes': 0,
                'distance_km': 0.0
            },
            {
                'name': 'Plank',
                'description': 'A core-strengthening exercise that also engages the shoulders, chest, and glutes.',
                'instructions': '1. Start in a push-up position with elbows bent. 2. Keep body in a straight line from head to heels. 3. Hold position for desired time.',
                'target_muscles': 'Core, Shoulders, Chest, Glutes',
                'repetitions': 0,
                'sets': 0,
                'duration_minutes': 2,
                'distance_km': 0.0
            },
            {
                'name': 'Side Plank',
                'description': 'A variation of the plank that targets the obliques and core stability.',
                'instructions': '1. Start in a plank position on side, supporting body with elbow and feet. 2. Keep body in straight line, holding position.',
                'target_muscles': 'Obliques, Core',
                'repetitions': 0,
                'sets': 0,
                'duration_minutes': 1,
                'distance_km': 0.0
            },
            {
                'name': 'Run',
                'description': 'A cardiovascular exercise that involves continuous running or jogging.',
                'instructions': '1. Start with a warm-up jog to prepare muscles. 2. Maintain a steady pace for the desired duration. 3. Cool down with a slower jog or walk.',
                'target_muscles': 'Legs, Cardiovascular System',
                'repetitions': 0,
                'sets': 0,
                'duration_minutes': 30,
                'distance_km': 5.0
            },
            {
                'name': 'Cycling',
                'description': 'A cardiovascular exercise that involves riding a bicycle.',
                'instructions': '1. Start with a warm-up ride to prepare muscles. 2. Maintain a steady pace for the desired duration. 3. Gradually increase resistance for more intensity. 4. Cool down with a slower ride.',
                'target_muscles': 'Legs, Cardiovascular System',
                'repetitions': 0,
                'sets': 0,
                'duration_minutes': 45,
                'distance_km': 15.0
            }
        ]

        for exercise_data in exercises:
            Exercise.objects.create(**exercise_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated exercises.'))
