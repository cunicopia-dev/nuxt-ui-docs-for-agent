<!-- source: https://ui.nuxt.com/components/calendar --> # Calendar

[Calendar](https://reka-
ui.com/docs/components/calendar)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Calendar.vue)

A calendar component for selecting single dates, multiple dates or date
ranges.

This component relies on the [`@internationalized/date`](https://react-
spectrum.adobe.com/internationalized/date/index.html) package which provides
objects and functions for representing and manipulating dates and times in a
locale-aware manner.

## Usage

Use the `v-model` directive to control the selected date.

February 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
  
Event Date, February 2022

    
    
    <script setup lang="ts">
    const value = ref(new CalendarDate(2022, 2, 3))
    </script>
    
    <template>
      <UCalendar v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

February 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
  
Event Date, February 2022

    
    
    <script setup lang="ts">
    const defaultValue = ref(new CalendarDate(2022, 2, 6))
    </script>
    
    <template>
      <UCalendar :default-value="defaultValue" />
    </template>
    

### Multiple

Use the `multiple` prop to allow multiple selections.

February 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
  
Event Date, February 2022

    
    
    <script setup lang="ts">
    const value = ref([
      new CalendarDate(2022, 2, 4),
      new CalendarDate(2022, 2, 6),
      new CalendarDate(2022, 2, 8)
    ])
    </script>
    
    <template>
      <UCalendar multiple v-model="value" />
    </template>
    

### Range

Use the `range` prop to select a range of dates.

Event Date, February 2022

February 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
      
    
    <script setup lang="ts">
    const value = ref({ start: new CalendarDate(2022, 2, 3), end: new CalendarDate(2022, 2, 20) })
    </script>
    
    <template>
      <UCalendar range v-model="value" />
    </template>
    

### Color

Use the `color` prop to change the color of the calendar.

color

neutral

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar color="neutral" />
    </template>
    

### Size

Use the `size` prop to change the size of the calendar.

size

xl

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar size="xl" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the calendar.

disabled

true

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar disabled />
    </template>
    

### Number Of Months

Use the `numberOfMonths` prop to change the number of months in the calendar.

numberOfMonths

April - June 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
11| 12| 13| 14| 15| 16| 17  
18| 19| 20| 21| 22| 23| 24  
25| 26| 27| 28| 29| 30| 31  
1| 2| 3| 4| 5| 6| 7  
S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
1| 2| 3| 4| 5| 6| 7  
8| 9| 10| 11| 12| 13| 14  
15| 16| 17| 18| 19| 20| 21  
22| 23| 24| 25| 26| 27| 28  
29| 30| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
  
Event Date, April - June 2025

    
    
    <template>
      <UCalendar :number-of-months="3" />
    </template>
    

### Month Controls

Use the `month-controls` prop to show the month controls. Defaults to `true`.

monthControls

false

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar :month-controls="false" />
    </template>
    

### Year Controls

Use the `year-controls` prop to show the year controls. Defaults to `true`.

yearControls

false

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar :year-controls="false" />
    </template>
    

### Fixed Weeks

Use the `fixed-weeks` prop to display the calendar with fixed weeks.

fixedWeeks

false

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
  
Event Date, April 2025

    
    
    <template>
      <UCalendar :fixed-weeks="false" />
    </template>
    

## Examples

### With chip events

Use the [Chip](/components/chip) component to add events to specific days.

January 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
26| 27| 28| 29| 30| 31| 1  
2| 3| 4| 5| 6| 7| 8  
9| 10| 11| 12| 13| 14| 15  
16| 17| 18| 19| 20| 21| 22  
23| 24| 25| 26| 27| 28| 29  
30| 31| 1| 2| 3| 4| 5  
  
Event Date, January 2022

    
    
    <script setup lang="ts">
    import { CalendarDate } from '@internationalized/date'
    
    const modelValue = shallowRef(new CalendarDate(2022, 1, 10))
    
    function getColorByDate(date: Date) {
      const isWeekend = date.getDay() % 6 == 0
      const isDayMeeting = date.getDay() % 3 == 0
    
      if (isWeekend) {
        return undefined
      }
    
      if (isDayMeeting) {
        return 'error'
      }
    
      return 'success'
    }
    </script>
    
    <template>
      <UCalendar v-model="modelValue">
        <template #day="{ day }">
          <UChip :show="!!getColorByDate(day.toDate('UTC'))" :color="getColorByDate(day.toDate('UTC'))" size="2xs">
            {{ day.day }}
          </UChip>
        </template>
      </UCalendar>
    </template>
    

### With disabled dates

Use the `is-date-disabled` prop with a function to mark specific dates as
disabled.

Event Date, January 2022

January 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
26| 27| 28| 29| 30| 31| 1  
2| 3| 4| 5| 6| 7| 8  
9| 10| 11| 12| 13| 14| 15  
16| 17| 18| 19| 20| 21| 22  
23| 24| 25| 26| 27| 28| 29  
30| 31| 1| 2| 3| 4| 5  
      
    
    <script setup lang="ts">
    import type { DateValue } from '@internationalized/date'
    import { CalendarDate } from '@internationalized/date'
    
    const modelValue = shallowRef({
      start: new CalendarDate(2022, 1, 1),
      end: new CalendarDate(2022, 1, 9)
    })
    
    const isDateDisabled = (date: DateValue) => {
      return date.day >= 10 && date.day <= 16
    }
    </script>
    
    <template>
      <UCalendar v-model="modelValue" :is-date-disabled="isDateDisabled" range />
    </template>
    

### With unavailable dates

Use the `is-date-unavailable` prop with a function to mark specific dates as
unavailable.

Event Date, January 2022

January 2022

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
26| 27| 28| 29| 30| 31| 1  
2| 3| 4| 5| 6| 7| 8  
9| 10| 11| 12| 13| 14| 15  
16| 17| 18| 19| 20| 21| 22  
23| 24| 25| 26| 27| 28| 29  
30| 31| 1| 2| 3| 4| 5  
      
    
    <script setup lang="ts">
    import type { DateValue } from '@internationalized/date'
    import { CalendarDate } from '@internationalized/date'
    
    const modelValue = shallowRef({
      start: new CalendarDate(2022, 1, 1),
      end: new CalendarDate(2022, 1, 9)
    })
    
    const isDateUnavailable = (date: DateValue) => {
      return date.day >= 10 && date.day <= 16
    }
    </script>
    
    <template>
      <UCalendar v-model="modelValue" :is-date-unavailable="isDateUnavailable" range />
    </template>
    

### With min/max dates

Use the `min-value` and `max-value` props to limit the dates.

September 2023

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
27| 28| 29| 30| 31| 1| 2  
3| 4| 5| 6| 7| 8| 9  
10| 11| 12| 13| 14| 15| 16  
17| 18| 19| 20| 21| 22| 23  
24| 25| 26| 27| 28| 29| 30  
1| 2| 3| 4| 5| 6| 7  
  
Event Date, September 2023

    
    
    <script setup lang="ts">
    import { CalendarDate } from '@internationalized/date'
    
    const modelValue = shallowRef(new CalendarDate(2023, 9, 10))
    const minDate = new CalendarDate(2023, 9, 1)
    const maxDate = new CalendarDate(2023, 9, 30)
    </script>
    
    <template>
      <UCalendar v-model="modelValue" :min-value="minDate" :max-value="maxDate" />
    </template>
    

### With other calendar systems

You can use other calenders from `@internationalized/date` to implement a
different calendar system.

Tishri 5781

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
24| 25| 26| 27| 28| 29| 1  
2| 3| 4| 5| 6| 7| 8  
9| 10| 11| 12| 13| 14| 15  
16| 17| 18| 19| 20| 21| 22  
23| 24| 25| 26| 27| 28| 29  
30| 1| 2| 3| 4| 5| 6  
  
Event Date, Tishri 5781

    
    
    <script lang="ts" setup>
    import { CalendarDate, HebrewCalendar } from '@internationalized/date'
    
    const hebrewDate = shallowRef(new CalendarDate(new HebrewCalendar(), 5781, 1, 1))
    </script>
    
    <template>
      <UCalendar v-model="hebrewDate" />
    </template>
    

[](https://react-
spectrum.adobe.com/internationalized/date/Calendar.html#implementations)You
can check all the available calendars on `@internationalized/date` docs.

### With external controls

You can control the calendar with external controls by manipulating the date
passed in the `v-model`.

April 2025

S| M| T| W| T| F| S  
---|---|---|---|---|---|---  
30| 31| 1| 2| 3| 4| 5  
6| 7| 8| 9| 10| 11| 12  
13| 14| 15| 16| 17| 18| 19  
20| 21| 22| 23| 24| 25| 26  
27| 28| 29| 30| 1| 2| 3  
4| 5| 6| 7| 8| 9| 10  
  
Event Date, April 2025

Prev  Next

    
    
    <script setup lang="ts">
    import { CalendarDate } from '@internationalized/date'
    
    const date = shallowRef(new CalendarDate(2025, 4, 2))
    </script>
    
    <template>
      <div class="flex flex-col gap-4">
        <UCalendar v-model="date" :month-controls="false" :year-controls="false" />
    
        <div class="flex justify-between gap-4">
          <UButton color="neutral" variant="outline" @click="date = date.subtract({ months: 1 })">
            Prev
          </UButton>
    
          <UButton color="neutral" variant="outline" @click="date = date.add({ months: 1 })">
            Next
          </UButton>
        </div>
      </div>
    </template>
    

### As a DatePicker

Use a [Button](/components/button) and a [Popover](/components/popover)
component to create a date picker.

Jan 10, 2022

    
    
    <script setup lang="ts">
    import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
    
    const df = new DateFormatter('en-US', {
      dateStyle: 'medium'
    })
    
    const modelValue = shallowRef(new CalendarDate(2022, 1, 10))
    </script>
    
    <template>
      <UPopover>
        <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
          {{ modelValue ? df.format(modelValue.toDate(getLocalTimeZone())) : 'Select a date' }}
        </UButton>
    
        <template #content>
          <UCalendar v-model="modelValue" class="p-2" />
        </template>
      </UPopover>
    </template>
    

### As a DateRangePicker

Use a [Button](/components/button) and a [Popover](/components/popover)
component to create a date range picker.

Jan 20, 2022 - Feb 10, 2022

    
    
    <script setup lang="ts">
    import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
    
    const df = new DateFormatter('en-US', {
      dateStyle: 'medium'
    })
    
    const modelValue = shallowRef({
      start: new CalendarDate(2022, 1, 20),
      end: new CalendarDate(2022, 2, 10)
    })
    </script>
    
    <template>
      <UPopover>
        <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
          <template v-if="modelValue.start">
            <template v-if="modelValue.end">
              {{ df.format(modelValue.start.toDate(getLocalTimeZone())) }} - {{ df.format(modelValue.end.toDate(getLocalTimeZone())) }}
            </template>
    
            <template v-else>
              {{ df.format(modelValue.start.toDate(getLocalTimeZone())) }}
            </template>
          </template>
          <template v-else>
            Pick a date
          </template>
        </UButton>
    
        <template #content>
          <UCalendar v-model="modelValue" class="p-2" :number-of-months="2" range />
        </template>
      </UPopover>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`nextYearIcon`| `appConfig.ui.icons.chevronDoubleRight`| ` string`The icon to
use for the next year control.  
`nextYear`| | ` ButtonProps`Configure the next year button. `{ color: 'neutral', variant: 'ghost' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`Defaults to `'solid'`.
  * `activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`nextMonthIcon`| `appConfig.ui.icons.chevronRight`| ` string`The icon to use
for the next month control.  
`nextMonth`| | ` ButtonProps`Configure the next month button. `{ color: 'neutral', variant: 'ghost' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`Defaults to `'solid'`.
  * `activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`prevYearIcon`| `appConfig.ui.icons.chevronDoubleLeft`| ` string`The icon to
use for the previous year control.  
`prevYear`| | ` ButtonProps`Configure the prev year button. `{ color: 'neutral', variant: 'ghost' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`Defaults to `'solid'`.
  * `activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`prevMonthIcon`| `appConfig.ui.icons.chevronLeft`| ` string`The icon to use
for the previous month control.  
`prevMonth`| | ` ButtonProps`Configure the prev month button. `{ color: 'neutral', variant: 'ghost' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`Defaults to `'solid'`.
  * `activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`range`| | `boolean`Whether or not a range of dates can be selected  
`multiple`| | `boolean`Whether or not multiple dates can be selected  
`monthControls`| `true`| `boolean`Show month controls  
`yearControls`| `true`| `boolean`Show year controls  
`defaultValue`| | ` CalendarDate | CalendarDateTime | ZonedDateTime | DateRange | DateValue[]`Show properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `start: DateValue`
  * `end: DateValue`

  
`modelValue`| | ` null | CalendarDate | CalendarDateTime | ZonedDateTime | DateRange | DateValue[]`Show properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `start: DateValue`
  * `end: DateValue`

  
`defaultPlaceholder`| | ` CalendarDate | CalendarDateTime | ZonedDateTime`The default placeholder dateShow properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.

  
`placeholder`| | ` CalendarDate | CalendarDateTime | ZonedDateTime`The placeholder date, which is used to determine what month to display when no date is selected. This updates as the user navigates the calendar and can be used to programmatically control the calendar viewShow properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.

  
`allowNonContiguousRanges`| | `boolean`When combined with `isDateUnavailable`, determines whether non-contiguous ranges, i.e. ranges containing unavailable dates, may be selected.  
`pagedNavigation`| | `boolean`This property causes the previous and next buttons to navigate by the number of months displayed at once, rather than one month  
`preventDeselect`| | `boolean`Whether or not to prevent the user from deselecting a date without selecting another date first  
`weekStartsOn`| | ` 0 | 1 | 2 | 3 | 4 | 5 | 6`The day of the week to start the calendar on  
`weekdayFormat`| | ` "narrow" | "short" | "long"`The format to use for the weekday strings provided via the weekdays slot prop  
`fixedWeeks`| `true`| `boolean`Whether or not to always display 6 weeks in the
calendar  
`maxValue`| | ` CalendarDate | CalendarDateTime | ZonedDateTime`The maximum date that can be selectedShow properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.

  
`minValue`| | ` CalendarDate | CalendarDateTime | ZonedDateTime`The minimum date that can be selectedShow properties

  * `__#8@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `copy: () => CalendarDate`Returns a copy of this date.
  * `add: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateDuration) => CalendarDate`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields) => CalendarDate`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields, amount: number, options?: CycleOptions | undefined) => CalendarDate`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: AnyCalendarDate) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#10@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `copy: () => CalendarDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => CalendarDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields) => CalendarDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => CalendarDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: (timeZone: string, disambiguation?: Disambiguation | undefined) => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.
  * `__#11@#private: any`
  * `calendar: Calendar`The calendar system associated with this date, e.g. Gregorian.
  * `era: string`The calendar era for this date, e.g. "BC" or "AD".
  * `year: number`The year of this date within the era.
  * `month: number`The month number within the year. Note that some calendar systems such as Hebrew may have a variable number of months per year. Therefore, month numbers may not always correspond to the same month names in different years.
  * `day: number`The day number within the month.
  * `hour: number`The hour in the day, numbered from 0 to 23.
  * `minute: number`The minute in the hour.
  * `second: number`The second in the minute.
  * `millisecond: number`The millisecond in the second.
  * `timeZone: string`The IANA time zone identifier that this date and time is represented in.
  * `offset: number`The UTC offset for this time, in milliseconds.
  * `copy: () => ZonedDateTime`Returns a copy of this date.
  * `add: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration added to it.
  * `subtract: (duration: DateTimeDuration) => ZonedDateTime`Returns a new `CalendarDate` with the given duration subtracted from it.
  * `set: (fields: DateFields & TimeFields, disambiguation?: Disambiguation | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given fields set to the provided values. Other fields will be constrained accordingly.
  * `cycle: (field: keyof DateFields | keyof TimeFields, amount: number, options?: CycleTimeOptions | undefined) => ZonedDateTime`Returns a new `CalendarDate` with the given field adjusted by a specified amount. When the resulting value reaches the limits of the field, it wraps around.
  * `toDate: () => Date`Converts the date to a native JavaScript Date object, with the time set to midnight in the given time zone.
  * `toString: () => string`Converts the date to an ISO 8601 formatted string.
  * `toAbsoluteString: () => string`Converts the date to an ISO 8601 formatted string in UTC.
  * `compare: (b: CalendarDate | CalendarDateTime | ZonedDateTime) => number`Compares this date with another. A negative result indicates that this date is before the given one, and a positive date indicates that it is after.

  
`numberOfMonths`| | ` number`The number of months to display at once  
`disabled`| | `boolean`Whether or not the calendar is disabled  
`readonly`| | `boolean`Whether or not the calendar is readonly  
`initialFocus`| | `boolean`If true, the calendar will focus the selected day, today, or the first day of the month depending on what is visible when the calendar is mounted  
`isDateDisabled`| | ` (date: DateValue): boolean`A function that returns whether or not a date is disabled  
`isDateUnavailable`| | ` (date: DateValue): boolean`A function that returns whether or not a date is unavailable  
`nextPage`| | ` (placeholder: DateValue): DateValue`A function that returns the next page of the calendar. It receives the current placeholder as an argument inside the component.  
`prevPage`| | ` (placeholder: DateValue): DateValue`A function that returns the previous page of the calendar. It receives the current placeholder as an argument inside the component.  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; heading?: ClassNameValue; grid?: ClassNameValue; ... 5 more ...; cellTrigger?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`heading`| `{ value: string; }`  
`day`| `Pick<CalendarCellTriggerProps, "day">`  
`week-day`| `{ day: string; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[date: DateValue | DateRange | DateValue[] | null | undefined]`  
`update:placeholder`| `[date: DateValue] & [date: DateValue]`  
`update:startValue`| `[date: DateValue | undefined]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        calendar: {
          slots: {
            root: '',
            header: 'flex items-center justify-between',
            body: 'flex flex-col space-y-4 pt-4 sm:flex-row sm:space-x-4 sm:space-y-0',
            heading: 'text-center font-medium truncate mx-auto',
            grid: 'w-full border-collapse select-none space-y-1 focus:outline-none',
            gridRow: 'grid grid-cols-7',
            gridWeekDaysRow: 'mb-1 grid w-full grid-cols-7',
            gridBody: 'grid',
            headCell: 'rounded-md',
            cell: 'relative text-center',
            cellTrigger: [
              'm-0.5 relative flex items-center justify-center rounded-full whitespace-nowrap focus-visible:ring-2 focus:outline-none data-disabled:text-muted data-unavailable:line-through data-unavailable:text-muted data-unavailable:pointer-events-none data-[selected]:text-inverted data-today:font-semibold data-[outside-view]:text-muted',
              'transition'
            ]
          },
          variants: {
            color: {
              primary: {
                headCell: 'text-primary',
                cellTrigger: 'focus-visible:ring-primary data-[selected]:bg-primary data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
              },
              secondary: {
                headCell: 'text-secondary',
                cellTrigger: 'focus-visible:ring-secondary data-[selected]:bg-secondary data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
              },
              success: {
                headCell: 'text-success',
                cellTrigger: 'focus-visible:ring-success data-[selected]:bg-success data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
              },
              info: {
                headCell: 'text-info',
                cellTrigger: 'focus-visible:ring-info data-[selected]:bg-info data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
              },
              warning: {
                headCell: 'text-warning',
                cellTrigger: 'focus-visible:ring-warning data-[selected]:bg-warning data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
              },
              error: {
                headCell: 'text-error',
                cellTrigger: 'focus-visible:ring-error data-[selected]:bg-error data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
              },
              neutral: {
                headCell: 'text-highlighted',
                cellTrigger: 'focus-visible:ring-inverted data-[selected]:bg-inverted data-today:not-data-[selected]:text-inverted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
              }
            },
            size: {
              xs: {
                heading: 'text-xs',
                cell: 'text-xs',
                headCell: 'text-[10px]',
                cellTrigger: 'size-7',
                body: 'space-y-2 pt-2'
              },
              sm: {
                heading: 'text-xs',
                headCell: 'text-xs',
                cell: 'text-xs',
                cellTrigger: 'size-7'
              },
              md: {
                heading: 'text-sm',
                headCell: 'text-xs',
                cell: 'text-sm',
                cellTrigger: 'size-8'
              },
              lg: {
                heading: 'text-md',
                headCell: 'text-md',
                cellTrigger: 'size-9 text-md'
              },
              xl: {
                heading: 'text-lg',
                headCell: 'text-lg',
                cellTrigger: 'size-10 text-lg'
              }
            }
          },
          defaultVariants: {
            size: 'md',
            color: 'primary'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            calendar: {
              slots: {
                root: '',
                header: 'flex items-center justify-between',
                body: 'flex flex-col space-y-4 pt-4 sm:flex-row sm:space-x-4 sm:space-y-0',
                heading: 'text-center font-medium truncate mx-auto',
                grid: 'w-full border-collapse select-none space-y-1 focus:outline-none',
                gridRow: 'grid grid-cols-7',
                gridWeekDaysRow: 'mb-1 grid w-full grid-cols-7',
                gridBody: 'grid',
                headCell: 'rounded-md',
                cell: 'relative text-center',
                cellTrigger: [
                  'm-0.5 relative flex items-center justify-center rounded-full whitespace-nowrap focus-visible:ring-2 focus:outline-none data-disabled:text-muted data-unavailable:line-through data-unavailable:text-muted data-unavailable:pointer-events-none data-[selected]:text-inverted data-today:font-semibold data-[outside-view]:text-muted',
                  'transition'
                ]
              },
              variants: {
                color: {
                  primary: {
                    headCell: 'text-primary',
                    cellTrigger: 'focus-visible:ring-primary data-[selected]:bg-primary data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
                  },
                  secondary: {
                    headCell: 'text-secondary',
                    cellTrigger: 'focus-visible:ring-secondary data-[selected]:bg-secondary data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
                  },
                  success: {
                    headCell: 'text-success',
                    cellTrigger: 'focus-visible:ring-success data-[selected]:bg-success data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
                  },
                  info: {
                    headCell: 'text-info',
                    cellTrigger: 'focus-visible:ring-info data-[selected]:bg-info data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
                  },
                  warning: {
                    headCell: 'text-warning',
                    cellTrigger: 'focus-visible:ring-warning data-[selected]:bg-warning data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
                  },
                  error: {
                    headCell: 'text-error',
                    cellTrigger: 'focus-visible:ring-error data-[selected]:bg-error data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
                  },
                  neutral: {
                    headCell: 'text-highlighted',
                    cellTrigger: 'focus-visible:ring-inverted data-[selected]:bg-inverted data-today:not-data-[selected]:text-inverted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
                  }
                },
                size: {
                  xs: {
                    heading: 'text-xs',
                    cell: 'text-xs',
                    headCell: 'text-[10px]',
                    cellTrigger: 'size-7',
                    body: 'space-y-2 pt-2'
                  },
                  sm: {
                    heading: 'text-xs',
                    headCell: 'text-xs',
                    cell: 'text-xs',
                    cellTrigger: 'size-7'
                  },
                  md: {
                    heading: 'text-sm',
                    headCell: 'text-xs',
                    cell: 'text-sm',
                    cellTrigger: 'size-8'
                  },
                  lg: {
                    heading: 'text-md',
                    headCell: 'text-md',
                    cellTrigger: 'size-9 text-md'
                  },
                  xl: {
                    heading: 'text-lg',
                    headCell: 'text-lg',
                    cellTrigger: 'size-10 text-lg'
                  }
                }
              },
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            calendar: {
              slots: {
                root: '',
                header: 'flex items-center justify-between',
                body: 'flex flex-col space-y-4 pt-4 sm:flex-row sm:space-x-4 sm:space-y-0',
                heading: 'text-center font-medium truncate mx-auto',
                grid: 'w-full border-collapse select-none space-y-1 focus:outline-none',
                gridRow: 'grid grid-cols-7',
                gridWeekDaysRow: 'mb-1 grid w-full grid-cols-7',
                gridBody: 'grid',
                headCell: 'rounded-md',
                cell: 'relative text-center',
                cellTrigger: [
                  'm-0.5 relative flex items-center justify-center rounded-full whitespace-nowrap focus-visible:ring-2 focus:outline-none data-disabled:text-muted data-unavailable:line-through data-unavailable:text-muted data-unavailable:pointer-events-none data-[selected]:text-inverted data-today:font-semibold data-[outside-view]:text-muted',
                  'transition'
                ]
              },
              variants: {
                color: {
                  primary: {
                    headCell: 'text-primary',
                    cellTrigger: 'focus-visible:ring-primary data-[selected]:bg-primary data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
                  },
                  secondary: {
                    headCell: 'text-secondary',
                    cellTrigger: 'focus-visible:ring-secondary data-[selected]:bg-secondary data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
                  },
                  success: {
                    headCell: 'text-success',
                    cellTrigger: 'focus-visible:ring-success data-[selected]:bg-success data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
                  },
                  info: {
                    headCell: 'text-info',
                    cellTrigger: 'focus-visible:ring-info data-[selected]:bg-info data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
                  },
                  warning: {
                    headCell: 'text-warning',
                    cellTrigger: 'focus-visible:ring-warning data-[selected]:bg-warning data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
                  },
                  error: {
                    headCell: 'text-error',
                    cellTrigger: 'focus-visible:ring-error data-[selected]:bg-error data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
                  },
                  neutral: {
                    headCell: 'text-highlighted',
                    cellTrigger: 'focus-visible:ring-inverted data-[selected]:bg-inverted data-today:not-data-[selected]:text-inverted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
                  }
                },
                size: {
                  xs: {
                    heading: 'text-xs',
                    cell: 'text-xs',
                    headCell: 'text-[10px]',
                    cellTrigger: 'size-7',
                    body: 'space-y-2 pt-2'
                  },
                  sm: {
                    heading: 'text-xs',
                    headCell: 'text-xs',
                    cell: 'text-xs',
                    cellTrigger: 'size-7'
                  },
                  md: {
                    heading: 'text-sm',
                    headCell: 'text-xs',
                    cell: 'text-sm',
                    cellTrigger: 'size-8'
                  },
                  lg: {
                    heading: 'text-md',
                    headCell: 'text-md',
                    cellTrigger: 'size-9 text-md'
                  },
                  xl: {
                    heading: 'text-lg',
                    headCell: 'text-lg',
                    cellTrigger: 'size-10 text-lg'
                  }
                }
              },
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ButtonGroupGroup multiple button-like elements together.](/components/button-
group)[CardDisplay content in a card with a header, body and
footer.](/components/card)

