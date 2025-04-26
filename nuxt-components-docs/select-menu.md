<!-- source: https://ui.nuxt.com/components/select-menu --> # SelectMenu

[Combobox](https://reka-
ui.com/docs/components/combobox)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/SelectMenu.vue)

An advanced searchable select element.

## Usage

Use the `v-model` directive to control the value of the SelectMenu or the
`default-value` prop to set the initial value when you do not need to control
its state.

Use this over a [`Select`](/components/select) to take advantage of Reka UI's
[`Combobox`](https://reka-ui.com/docs/components/combobox) component that
offers search capabilities and multiple selection.

This component is similar to the [`InputMenu`](/components/input-menu) but
it's using a Select instead of an Input with the search inside the menu.

### Items

Use the `items` prop as an array of strings, numbers or booleans:

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" :items="items" class="w-48" />
    </template>
    

You can also pass an array of objects with the following properties:

  * `label?: string`
  * `type?: "label" | "separator" | "item"`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `chip?: ChipProps`
  * `disabled?: boolean`
  * `onSelect?(e: Event): void`

Todo

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'Backlog'
      },
      {
        label: 'Todo'
      },
      {
        label: 'In Progress'
      },
      {
        label: 'Done'
      }
    ])
    const value = ref({
      label: 'Todo'
    })
    </script>
    
    <template>
      <USelectMenu v-model="value" :items="items" class="w-48" />
    </template>
    

Unlike the [`Select`](/components/select) component, the SelectMenu expects
the whole object to be passed to the `v-model` directive or the `default-
value` prop by default.

You can also pass an array of arrays to the `items` prop to display separated
groups of items.

Apple

    
    
    <script setup lang="ts">
    const items = ref([
      ['Apple', 'Banana', 'Blueberry', 'Grapes', 'Pineapple'],
      ['Aubergine', 'Broccoli', 'Carrot', 'Courgette', 'Leek']
    ])
    const value = ref('Apple')
    </script>
    
    <template>
      <USelectMenu v-model="value" :items="items" class="w-48" />
    </template>
    

### Value Key

You can choose to bind a single property of the object rather than the whole
object by using the `value-key` prop. Defaults to `undefined`.

Todo

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'Backlog',
        id: 'backlog'
      },
      {
        label: 'Todo',
        id: 'todo'
      },
      {
        label: 'In Progress',
        id: 'in_progress'
      },
      {
        label: 'Done',
        id: 'done'
      }
    ])
    const value = ref('todo')
    </script>
    
    <template>
      <USelectMenu v-model="value" value-key="id" :items="items" class="w-48" />
    </template>
    

Expand code

### Multiple

Use the `multiple` prop to allow multiple selections, the selected items will
be separated by a comma in the trigger.

Backlog, Todo

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref(['Backlog', 'Todo'])
    </script>
    
    <template>
      <USelectMenu v-model="value" multiple :items="items" class="w-48" />
    </template>
    

Ensure to pass an array to the `default-value` prop or the `v-model`
directive.

### Placeholder

Use the `placeholder` prop to set a placeholder text.

placeholder

Select status

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    </script>
    
    <template>
      <USelectMenu placeholder="Select status" :items="items" class="w-48" />
    </template>
    

### Search Input

Use the `search-input` prop to customize or hide the search input (with
`false` value).

You can pass any property from the [Input](/components/input) component to
customize it.

searchInput.placeholder

searchInput.icon

Backlog

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'Backlog',
        icon: 'i-lucide-circle-help'
      },
      {
        label: 'Todo',
        icon: 'i-lucide-circle-plus'
      },
      {
        label: 'In Progress',
        icon: 'i-lucide-circle-arrow-up'
      },
      {
        label: 'Done',
        icon: 'i-lucide-circle-check'
      }
    ])
    const value = ref({
      label: 'Backlog',
      icon: 'i-lucide-circle-help'
    })
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        :search-input="{
          placeholder: 'Filter...',
          icon: 'i-lucide-search'
        }"
        :items="items"
        class="w-48"
      />
    </template>
    

You can set the `search-input` prop to `false` to hide the search input.

### Content

Use the `content` prop to control how the SelectMenu content is rendered, like
its `align` or `side` for example.

content.align

center

content.side

bottom

content.sideOffset

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        :content="{
          align: 'center',
          side: 'bottom',
          sideOffset: 8
        }"
        :items="items"
        class="w-48"
      />
    </template>
    

### Arrow

Use the `arrow` prop to display an arrow on the SelectMenu.

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" arrow :items="items" class="w-48" />
    </template>
    

### Color

Use the `color` prop to change the ring color when the SelectMenu is focused.

color

neutral

highlight

true

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" color="neutral" highlight :items="items" class="w-48" />
    </template>
    

The `highlight` prop is used here to show the focus state. It's used
internally when a validation error occurs.

### Variant

Use the `variant` prop to change the variant of the SelectMenu.

color

neutral

variant

subtle

highlight

false

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" color="neutral" variant="subtle" :items="items" class="w-48" />
    </template>
    

### Size

Use the `size` prop to change the size of the SelectMenu.

size

xl

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" size="xl" :items="items" class="w-48" />
    </template>
    

### Icon

Use the `icon` prop to show an [Icon](/components/icon) inside the SelectMenu.

icon

size

md

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" icon="i-lucide-search" size="md" :items="items" class="w-48" />
    </template>
    

### Trailing Icon

Use the `trailing-icon` prop to customize the trailing
[Icon](/components/icon). Defaults to `i-lucide-chevron-down`.

trailingIcon

size

md

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        trailing-icon="i-lucide-arrow-down"
        size="md"
        :items="items"
        class="w-48"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.chevronDown` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.chevronDown` key.

### Selected Icon

Use the `selected-icon` prop to customize the icon when an item is selected.
Defaults to `i-lucide-check`.

selectedIcon

size

md

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        selected-icon="i-lucide-flame"
        size="md"
        :items="items"
        class="w-48"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.check` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.check` key.

### Avatar

Use the `avatar` prop to display an [Avatar](/components/avatar) inside the
SelectMenu.

avatar.src

![](https://github.com/nuxt.png)Nuxt

    
    
    <script setup lang="ts">
    const items = ref(['Nuxt', 'NuxtHub', 'NuxtLabs', 'Nuxt Modules', 'Nuxt Community'])
    const value = ref('Nuxt')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        :items="items"
        class="w-48"
      />
    </template>
    

### Loading

Use the `loading` prop to show a loading icon on the SelectMenu.

loading

true

trailing

false

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" loading :items="items" class="w-48" />
    </template>
    

### Loading Icon

Use the `loading-icon` prop to customize the loading icon. Defaults to
`i-lucide-refresh-cw`.

loading

true

loadingIcon

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        loading
        loading-icon="i-lucide-repeat-2"
        :items="items"
        class="w-48"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.loading` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.loading` key.

### Disabled

Use the `disabled` prop to disable the SelectMenu.

disabled

true

Select status

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    </script>
    
    <template>
      <USelectMenu disabled placeholder="Select status" :items="items" class="w-48" />
    </template>
    

## Examples

### With items type

You can use the `type` property with `separator` to display a separator
between items or `label` to display a label.

Apple

    
    
    <script setup lang="ts">
    const items = ref([
      {
        type: 'label',
        label: 'Fruits'
      },
      'Apple',
      'Banana',
      'Blueberry',
      'Grapes',
      'Pineapple',
      {
        type: 'separator'
      },
      {
        type: 'label',
        label: 'Vegetables'
      },
      'Aubergine',
      'Broccoli',
      'Carrot',
      'Courgette',
      'Leek'
    ])
    const value = ref('Apple')
    </script>
    
    <template>
      <USelectMenu v-model="value" :items="items" class="w-48" />
    </template>
    

Expand code

### With icons in items

You can use the `icon` property to display an [Icon](/components/icon) inside
the items.

Backlog

    
    
    <script setup lang="ts">
    import type { SelectMenuItem } from '@nuxt/ui'
    
    const items = ref([
      {
        label: 'Backlog',
        value: 'backlog',
        icon: 'i-lucide-circle-help'
      },
      {
        label: 'Todo',
        value: 'todo',
        icon: 'i-lucide-circle-plus'
      },
      {
        label: 'In Progress',
        value: 'in_progress',
        icon: 'i-lucide-circle-arrow-up'
      },
      {
        label: 'Done',
        value: 'done',
        icon: 'i-lucide-circle-check'
      }
    ] satisfies SelectMenuItem[])
    const value = ref(items.value[0])
    </script>
    
    <template>
      <USelectMenu v-model="value" :icon="value?.icon" :items="items" class="w-48" />
    </template>
    

Expand code

You can also use the `#leading` slot to display the selected icon.

### With avatar in items

You can use the `avatar` property to display an [Avatar](/components/avatar)
inside the items.

![benjamincanac](https://github.com/benjamincanac.png)benjamincanac

    
    
    <script setup lang="ts">
    import type { SelectMenuItem } from '@nuxt/ui'
    
    const items = ref([
      {
        label: 'benjamincanac',
        value: 'benjamincanac',
        avatar: {
          src: 'https://github.com/benjamincanac.png',
          alt: 'benjamincanac'
        }
      },
      {
        label: 'romhml',
        value: 'romhml',
        avatar: {
          src: 'https://github.com/romhml.png',
          alt: 'romhml'
        }
      },
      {
        label: 'noook',
        value: 'noook',
        avatar: {
          src: 'https://github.com/noook.png',
          alt: 'noook'
        }
      },
      {
        label: 'sandros94',
        value: 'sandros94',
        avatar: {
          src: 'https://github.com/sandros94.png',
          alt: 'sandros94'
        }
      }
    ] satisfies SelectMenuItem[])
    const value = ref(items.value[0])
    </script>
    
    <template>
      <USelectMenu v-model="value" :avatar="value?.avatar" :items="items" class="w-48" />
    </template>
    

Expand code

You can also use the `#leading` slot to display the selected avatar.

### With chip in items

You can use the `chip` property to display a [Chip](/components/chip) inside
the items.

bug

    
    
    <script setup lang="ts">
    import type { SelectMenuItem, ChipProps } from '@nuxt/ui'
    
    const items = ref([
      {
        label: 'bug',
        value: 'bug',
        chip: {
          color: 'error'
        }
      },
      {
        label: 'feature',
        value: 'feature',
        chip: {
          color: 'success'
        }
      },
      {
        label: 'enhancement',
        value: 'enhancement',
        chip: {
          color: 'info'
        }
      }
    ] satisfies SelectMenuItem[])
    const value = ref(items.value[0])
    </script>
    
    <template>
      <USelectMenu v-model="value" :items="items" class="w-48">
        <template #leading="{ modelValue, ui }">
          <UChip
            v-if="modelValue"
            v-bind="modelValue.chip"
            inset
            standalone
            :size="(ui.itemLeadingChipSize() as ChipProps['size'])"
            :class="ui.itemLeadingChip()"
          />
        </template>
      </USelectMenu>
    </template>
    

Expand code

In this example, the `#leading` slot is used to display the selected chip.

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Backlog

    
    
    <script setup lang="ts">
    const open = ref(false)
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <USelectMenu v-model="value" v-model:open="open" :items="items" class="w-48" />
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the SelectMenu by pressing `O`.

### Control search term

Use the `v-model:search-term` directive to control the search term.

Backlog

    
    
    <script setup lang="ts">
    const searchTerm = ref('D')
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu v-model="value" v-model:search-term="searchTerm" :items="items" class="w-48" />
    </template>
    

### With rotating icon

Here is an example with a rotating icon that indicates the open state of the
SelectMenu.

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        :items="items"
        :ui="{
          trailingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200'
        }"
        class="w-48"
      />
    </template>
    

### With create item

Use the `create-item` prop to enable users to add custom values that aren't in
the predefined options.

Backlog

    
    
    <script setup lang="ts">
    const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
    const value = ref('Backlog')
    
    function onCreate(item: string) {
      items.value.push(item)
    
      value.value = item
    }
    </script>
    
    <template>
      <USelectMenu
        v-model="value"
        create-item
        :items="items"
        class="w-48"
        @create="onCreate"
      />
    </template>
    

Expand code

The create option shows when no match is found by default. Set it to `always`
to show it even when similar values exist.

Use the `@create` event to handle the creation of the item. You will receive
the event and the item as arguments.

### With fetched items

You can fetch items from an API and use them in the SelectMenu.

Select user

    
    
    <script setup lang="ts">
    import type { AvatarProps } from '@nuxt/ui'
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'typicode-users',
      transform: (data: { id: number, name: string }[]) => {
        return data?.map(user => ({
          label: user.name,
          value: String(user.id),
          avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` }
        }))
      },
      lazy: true
    })
    </script>
    
    <template>
      <USelectMenu
        :items="users"
        :loading="status === 'pending'"
        icon="i-lucide-user"
        placeholder="Select user"
        class="w-48"
      >
        <template #leading="{ modelValue, ui }">
          <UAvatar
            v-if="modelValue"
            v-bind="modelValue.avatar"
            :size="(ui.leadingAvatarSize() as AvatarProps['size'])"
            :class="ui.leadingAvatar()"
          />
        </template>
      </USelectMenu>
    </template>
    

Expand code

### With ignore filter

Set the `ignore-filter` prop to `true` to disable the internal search and use
your own search logic.

Select user

    
    
    <script setup lang="ts">
    import type { AvatarProps } from '@nuxt/ui'
    
    const searchTerm = ref('')
    const searchTermDebounced = refDebounced(searchTerm, 200)
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'typicode-users',
      params: { q: searchTermDebounced },
      transform: (data: { id: number, name: string }[]) => {
        return data?.map(user => ({
          label: user.name,
          value: String(user.id),
          avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` }
        }))
      },
      lazy: true
    })
    </script>
    
    <template>
      <USelectMenu
        v-model:search-term="searchTerm"
        :items="users"
        :loading="status === 'pending'"
        ignore-filter
        icon="i-lucide-user"
        placeholder="Select user"
        class="w-48"
      >
        <template #leading="{ modelValue, ui }">
          <UAvatar
            v-if="modelValue"
            v-bind="modelValue.avatar"
            :size="(ui.leadingAvatarSize() as AvatarProps['size'])"
            :class="ui.leadingAvatar()"
          />
        </template>
      </USelectMenu>
    </template>
    

Expand code

This example uses
[`refDebounced`](https://vueuse.org/shared/refDebounced/#refdebounced) to
debounce the API calls.

### With filter fields

Use the `filter-fields` prop with an array of fields to filter on. Defaults to
`[labelKey]`.

Select user

    
    
    <script setup lang="ts">
    import type { AvatarProps } from '@nuxt/ui'
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'typicode-users-email',
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({
          label: user.name,
          email: user.email,
          value: String(user.id),
          avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` }
        }))
      },
      lazy: true
    })
    </script>
    
    <template>
      <USelectMenu
        :items="users"
        :loading="status === 'pending'"
        :filter-fields="['label', 'email']"
        icon="i-lucide-user"
        placeholder="Select user"
        class="w-80"
      >
        <template #leading="{ modelValue, ui }">
          <UAvatar
            v-if="modelValue"
            v-bind="modelValue.avatar"
            :size="(ui.leadingAvatarSize() as AvatarProps['size'])"
            :class="ui.leadingAvatar()"
          />
        </template>
    
        <template #item-label="{ item }">
          {{ item.label }}
    
          <span class="text-muted">
            {{ item.email }}
          </span>
        </template>
      </USelectMenu>
    </template>
    

Expand code

### As a CountryPicker

This example demonstrates using the SelectMenu as a country picker with lazy
loading - countries are only fetched when the menu is opened.

Select country

    
    
    <script setup lang="ts">
    const { data: countries, status, execute } = await useLazyFetch<{
      name: string
      code: string
      emoji: string
    }[]>('/api/countries.json', {
      immediate: false
    })
    
    function onOpen() {
      if (!countries.value?.length) {
        execute()
      }
    }
    </script>
    
    <template>
      <USelectMenu
        :items="countries"
        :loading="status === 'pending'"
        label-key="name"
        :search-input="{ icon: 'i-lucide-search' }"
        placeholder="Select country"
        class="w-48"
        @update:open="onOpen"
      >
        <template #leading="{ modelValue, ui }">
          <span v-if="modelValue" class="size-5 text-center">
            {{ modelValue?.emoji }}
          </span>
          <UIcon v-else name="i-lucide-earth" :class="ui.leadingIcon()" />
        </template>
        <template #item-leading="{ item }">
          <span class="size-5 text-center">
            {{ item.emoji }}
          </span>
        </template>
      </USelectMenu>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`id`| | ` string`  
`placeholder`| | ` string`The placeholder text when the select is empty.  
`searchInput`| `true`| `boolean | InputProps`Whether to display the search input or not. Can be an object to pass additional props to the input. `{ placeholder: 'Search...', variant: 'none' }`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `id?: string`
  * `name?: string`
  * `type?: InputTypeHTMLAttribute`
  * `placeholder?: string`The placeholder text when the input is empty.
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `variant?: "outline" | "soft" | "subtle" | "ghost" | "none"`Defaults to `'outline'`.
  * `size?: "sm" | "md" | "xs" | "lg" | "xl"`Defaults to `'md'`.
  * `required?: boolean`
  * `autocomplete?: string`
  * `autofocus?: boolean`
  * `autofocusDelay?: number`
  * `disabled?: boolean`
  * `highlight?: boolean`Highlight the ring color like a focus state.
  * `class?: any`
  * `ui?: { root?: ClassNameValue; base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`required`| | `boolean`  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
to open the menu.  
`selectedIcon`| `appConfig.ui.icons.check`| ` string`The icon displayed when
an item is selected.  
`content`| `{ side: 'bottom', sideOffset: 8, collisionPadding: 8, position: 'popper' }`| ` Omit<ComboboxContentProps, "asChild" | "as" | "forceMount"> & Partial<EmitsToProps<DismissableLayerEmits>>`The content of the menu.Show properties

  * `position?: "inline" | "popper"`The positioning mode to use,   
`inline` is the default and you can control the position using CSS.  
`popper` positions content in the same way as our other primitives, for
example `Popover` or `DropdownMenu`.

  * `bodyLock?: boolean`The document.body will be lock, and scrolling will be disabled.
  * `side?: "top" | "bottom" | "right" | "left"`The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled. Defaults to `"top"`.
  * `sideOffset?: number`The distance in pixels from the trigger. Defaults to `0`.
  * `align?: "start" | "center" | "end"`The preferred alignment against the trigger. May change when collisions occur. Defaults to `"center"`.
  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"top" | "bottom" | "right" | "left", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `arrowPadding?: number`The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to `0`.
  * `sticky?: "always" | "partial"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `updatePositionStrategy?: "always" | "optimized"`Strategy to update the position of the floating element on every animation frame. Defaults to `'optimized'`.
  * `disableUpdateOnLayoutShift?: boolean`Whether to disable the update position for the content when the layout shifted. Defaults to `false`.
  * `prioritizePosition?: boolean`Force content to be position within the viewport.Might overlap the reference element, which may not be desired. Defaults to `false`.
  * `reference?: ReferenceElement`The custom element or virtual element that will be set as the reference to position the floating element.If provided, it will replace the default anchor element.
  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`

  
`arrow`| `false`| `boolean | Omit<ComboboxArrowProps, "asChild" | "as">`Display an arrow alongside the menu.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the menu in a portal.  
`valueKey`| `undefined`| ` string | number`When `items` is an array of objects, select the field to use as the value instead of the object itself.  
`labelKey`| `'label'`| `undefined`When `items` is an array of objects, select
the field to use as the label.  
`items`| | ` SelectMenuItem[] | SelectMenuItem[][]`Show properties

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `chip?: ChipProps`
  * `type?: "label" | "separator" | "item"`The item type. Defaults to `'item'`.
  * `disabled?: boolean`
  * `onSelect?: ((e?: Event ) => void) | undefined`

  
`defaultValue`| | `any`The value of the SelectMenu when initially rendered. Use when you do not need to control the state of the SelectMenu.  
`modelValue`| | `any`The controlled value of the SelectMenu. Can be binded-with with `v-model`.  
`multiple`| | `boolean`Whether multiple options can be selected or not.  
`highlight`| | `boolean`Highlight the ring color like a focus state.  
`createItem`| `false`| `boolean | "always" | { position?: "top" | "bottom" ; when?: "always" | "empty" | undefined; } | undefined`Determines if custom user input that does not exist in options can be added.Show properties

  * `position?: "top" | "bottom"`
  * `when?: "always" | "empty"`

  
`filterFields`| `[labelKey]`| ` string[]`Fields to filter items by.  
`ignoreFilter`| `false`| `boolean`When `true`, disable the default filters,
useful for custom filtering (useAsyncData, useFetch, etc.).  
`open`| | `boolean`The controlled open state of the Combobox. Can be binded with with `v-model:open`.  
`defaultOpen`| | `boolean`The open state of the combobox when it is initially rendered.   
Use when you do not need to control its open state.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with listbox  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`resetSearchTermOnBlur`| `true`| `boolean`Whether to reset the searchTerm when
the Combobox input blurred  
`resetSearchTermOnSelect`| `true`| `boolean`Whether to reset the searchTerm
when the Combobox value is selected  
`highlightOnHover`| | `boolean`When `true`, hover over item will trigger highlight  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "3xs" | "sm" | "2xs" | "md" | "xs" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`leading`| | `boolean`When `true`, the icon will be displayed on the left side.  
`leadingIcon`| | ` string`Display an icon on the left side.  
`trailing`| | `boolean`When `true`, the icon will be displayed on the right side.  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`searchTerm`| `''`| ` string`  
`ui`| | ` { base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; ... 21 more ...; focusScope?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{ modelValue?: any; open: boolean; ui: { base: (props?: Record<string, any> | undefined) => string; leading: (props?: Record<string, any> | undefined) => string; leadingIcon: (props?: Record<...> | undefined) => string; ... 23 more ...; focusScope: (props?: Record<...> | undefined) => string; }; }`  
`default`| `{ modelValue?: any; open: boolean; }`  
`trailing`| `{ modelValue?: any; open: boolean; ui: { base: (props?: Record<string, any> | undefined) => string; leading: (props?: Record<string, any> | undefined) => string; leadingIcon: (props?: Record<...> | undefined) => string; ... 23 more ...; focusScope: (props?: Record<...> | undefined) => string; }; }`  
`empty`| `{ searchTerm?: string | undefined; }`  
`item`| `{ item: SelectMenuItem; index: number; }`  
`item-leading`| `{ item: SelectMenuItem; index: number; }`  
`item-label`| `{ item: SelectMenuItem; index: number; }`  
`item-trailing`| `{ item: SelectMenuItem; index: number; }`  
`content-top`| `{}`  
`content-bottom`| `{}`  
`create-item-label`| `{ item: string; }`  
  
### Emits

Event |  Type   
---|---  
`blur`| `[payload: FocusEvent]`  
`change`| `[payload: Event]`  
`focus`| `[payload: FocusEvent]`  
`update:open`| `[value: boolean]`  
`create`| `[item: string]`  
`highlight`| `[payload: { ref: HTMLElement; value: any; } | undefined]`  
`update:modelValue`| `[payload: any]`  
`update:searchTerm`| `[value: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        selectMenu: {
          slots: {
            base: [
              'relative group rounded-md inline-flex items-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ],
            leading: 'absolute inset-y-0 start-0 flex items-center',
            leadingIcon: 'shrink-0 text-dimmed',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            trailing: 'absolute inset-y-0 end-0 flex items-center',
            trailingIcon: 'shrink-0 text-dimmed',
            value: 'truncate pointer-events-none',
            placeholder: 'truncate text-dimmed',
            arrow: 'fill-default',
            content: [
              'max-h-60 w-(--reka-select-trigger-width) bg-default shadow-lg rounded-md ring ring-default overflow-hidden data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-select-content-transform-origin) pointer-events-auto',
              'origin-(--reka-combobox-content-transform-origin) w-(--reka-combobox-trigger-width)'
            ],
            viewport: 'divide-y divide-default scroll-py-1',
            group: 'p-1 isolate',
            empty: 'py-2 text-center text-sm text-muted',
            label: 'font-semibold text-highlighted',
            separator: '-mx-1 my-1 h-px bg-border',
            item: [
              'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75 text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
              'transition-colors before:transition-colors'
            ],
            itemLeadingIcon: [
              'shrink-0 text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
              'transition-colors'
            ],
            itemLeadingAvatar: 'shrink-0',
            itemLeadingAvatarSize: '',
            itemLeadingChip: 'shrink-0',
            itemLeadingChipSize: '',
            itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            itemTrailingIcon: 'shrink-0',
            itemLabel: 'truncate',
            input: 'border-b border-default',
            focusScope: 'flex flex-col min-h-0'
          },
          variants: {
            buttonGroup: {
              horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
              vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
            },
            size: {
              xs: {
                base: 'px-2 py-1 text-xs gap-1',
                leading: 'ps-2',
                trailing: 'pe-2',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4',
                label: 'p-1 text-[10px]/3 gap-1',
                item: 'p-1 text-xs gap-1',
                itemLeadingIcon: 'size-4',
                itemLeadingAvatarSize: '3xs',
                itemLeadingChip: 'size-4',
                itemLeadingChipSize: 'sm',
                itemTrailingIcon: 'size-4'
              },
              sm: {
                base: 'px-2.5 py-1.5 text-xs gap-1.5',
                leading: 'ps-2.5',
                trailing: 'pe-2.5',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4',
                label: 'p-1.5 text-[10px]/3 gap-1.5',
                item: 'p-1.5 text-xs gap-1.5',
                itemLeadingIcon: 'size-4',
                itemLeadingAvatarSize: '3xs',
                itemLeadingChip: 'size-4',
                itemLeadingChipSize: 'sm',
                itemTrailingIcon: 'size-4'
              },
              md: {
                base: 'px-2.5 py-1.5 text-sm gap-1.5',
                leading: 'ps-2.5',
                trailing: 'pe-2.5',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5',
                label: 'p-1.5 text-xs gap-1.5',
                item: 'p-1.5 text-sm gap-1.5',
                itemLeadingIcon: 'size-5',
                itemLeadingAvatarSize: '2xs',
                itemLeadingChip: 'size-5',
                itemLeadingChipSize: 'md',
                itemTrailingIcon: 'size-5'
              },
              lg: {
                base: 'px-3 py-2 text-sm gap-2',
                leading: 'ps-3',
                trailing: 'pe-3',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5',
                label: 'p-2 text-xs gap-2',
                item: 'p-2 text-sm gap-2',
                itemLeadingIcon: 'size-5',
                itemLeadingAvatarSize: '2xs',
                itemLeadingChip: 'size-5',
                itemLeadingChipSize: 'md',
                itemTrailingIcon: 'size-5'
              },
              xl: {
                base: 'px-3 py-2 text-base gap-2',
                leading: 'ps-3',
                trailing: 'pe-3',
                leadingIcon: 'size-6',
                leadingAvatarSize: 'xs',
                trailingIcon: 'size-6',
                label: 'p-2 text-sm gap-2',
                item: 'p-2 text-base gap-2',
                itemLeadingIcon: 'size-6',
                itemLeadingAvatarSize: 'xs',
                itemLeadingChip: 'size-6',
                itemLeadingChipSize: 'lg',
                itemTrailingIcon: 'size-6'
              }
            },
            variant: {
              outline: 'text-highlighted bg-default ring ring-inset ring-accented',
              soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
              subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
              ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
              none: 'text-highlighted bg-transparent'
            },
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            leading: {
              true: ''
            },
            trailing: {
              true: ''
            },
            loading: {
              true: ''
            },
            highlight: {
              true: ''
            },
            type: {
              file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
            },
            {
              color: 'primary',
              highlight: true,
              class: 'ring ring-inset ring-primary'
            },
            {
              color: 'neutral',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
            },
            {
              color: 'neutral',
              highlight: true,
              class: 'ring ring-inset ring-inverted'
            },
            {
              leading: true,
              size: 'xs',
              class: 'ps-7'
            },
            {
              leading: true,
              size: 'sm',
              class: 'ps-8'
            },
            {
              leading: true,
              size: 'md',
              class: 'ps-9'
            },
            {
              leading: true,
              size: 'lg',
              class: 'ps-10'
            },
            {
              leading: true,
              size: 'xl',
              class: 'ps-11'
            },
            {
              trailing: true,
              size: 'xs',
              class: 'pe-7'
            },
            {
              trailing: true,
              size: 'sm',
              class: 'pe-8'
            },
            {
              trailing: true,
              size: 'md',
              class: 'pe-9'
            },
            {
              trailing: true,
              size: 'lg',
              class: 'pe-10'
            },
            {
              trailing: true,
              size: 'xl',
              class: 'pe-11'
            },
            {
              loading: true,
              leading: true,
              class: {
                leadingIcon: 'animate-spin'
              }
            },
            {
              loading: true,
              leading: false,
              trailing: true,
              class: {
                trailingIcon: 'animate-spin'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary',
            variant: 'outline'
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
            selectMenu: {
              slots: {
                base: [
                  'relative group rounded-md inline-flex items-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute inset-y-0 start-0 flex items-center',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute inset-y-0 end-0 flex items-center',
                trailingIcon: 'shrink-0 text-dimmed',
                value: 'truncate pointer-events-none',
                placeholder: 'truncate text-dimmed',
                arrow: 'fill-default',
                content: [
                  'max-h-60 w-(--reka-select-trigger-width) bg-default shadow-lg rounded-md ring ring-default overflow-hidden data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-select-content-transform-origin) pointer-events-auto',
                  'origin-(--reka-combobox-content-transform-origin) w-(--reka-combobox-trigger-width)'
                ],
                viewport: 'divide-y divide-default scroll-py-1',
                group: 'p-1 isolate',
                empty: 'py-2 text-center text-sm text-muted',
                label: 'font-semibold text-highlighted',
                separator: '-mx-1 my-1 h-px bg-border',
                item: [
                  'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75 text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ],
                itemLeadingIcon: [
                  'shrink-0 text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
                  'transition-colors'
                ],
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '',
                itemLeadingChip: 'shrink-0',
                itemLeadingChipSize: '',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0',
                itemLabel: 'truncate',
                input: 'border-b border-default',
                focusScope: 'flex flex-col min-h-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2',
                    trailing: 'pe-2',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4',
                    label: 'p-1 text-[10px]/3 gap-1',
                    item: 'p-1 text-xs gap-1',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemLeadingChip: 'size-4',
                    itemLeadingChipSize: 'sm',
                    itemTrailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4',
                    label: 'p-1.5 text-[10px]/3 gap-1.5',
                    item: 'p-1.5 text-xs gap-1.5',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemLeadingChip: 'size-4',
                    itemLeadingChipSize: 'sm',
                    itemTrailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5',
                    label: 'p-1.5 text-xs gap-1.5',
                    item: 'p-1.5 text-sm gap-1.5',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemLeadingChip: 'size-5',
                    itemLeadingChipSize: 'md',
                    itemTrailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5',
                    label: 'p-2 text-xs gap-2',
                    item: 'p-2 text-sm gap-2',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemLeadingChip: 'size-5',
                    itemLeadingChipSize: 'md',
                    itemTrailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6',
                    label: 'p-2 text-sm gap-2',
                    item: 'p-2 text-base gap-2',
                    itemLeadingIcon: 'size-6',
                    itemLeadingAvatarSize: 'xs',
                    itemLeadingChip: 'size-6',
                    itemLeadingChipSize: 'lg',
                    itemTrailingIcon: 'size-6'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                },
                {
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
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
            selectMenu: {
              slots: {
                base: [
                  'relative group rounded-md inline-flex items-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute inset-y-0 start-0 flex items-center',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute inset-y-0 end-0 flex items-center',
                trailingIcon: 'shrink-0 text-dimmed',
                value: 'truncate pointer-events-none',
                placeholder: 'truncate text-dimmed',
                arrow: 'fill-default',
                content: [
                  'max-h-60 w-(--reka-select-trigger-width) bg-default shadow-lg rounded-md ring ring-default overflow-hidden data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-select-content-transform-origin) pointer-events-auto',
                  'origin-(--reka-combobox-content-transform-origin) w-(--reka-combobox-trigger-width)'
                ],
                viewport: 'divide-y divide-default scroll-py-1',
                group: 'p-1 isolate',
                empty: 'py-2 text-center text-sm text-muted',
                label: 'font-semibold text-highlighted',
                separator: '-mx-1 my-1 h-px bg-border',
                item: [
                  'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75 text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ],
                itemLeadingIcon: [
                  'shrink-0 text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
                  'transition-colors'
                ],
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '',
                itemLeadingChip: 'shrink-0',
                itemLeadingChipSize: '',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0',
                itemLabel: 'truncate',
                input: 'border-b border-default',
                focusScope: 'flex flex-col min-h-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2',
                    trailing: 'pe-2',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4',
                    label: 'p-1 text-[10px]/3 gap-1',
                    item: 'p-1 text-xs gap-1',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemLeadingChip: 'size-4',
                    itemLeadingChipSize: 'sm',
                    itemTrailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4',
                    label: 'p-1.5 text-[10px]/3 gap-1.5',
                    item: 'p-1.5 text-xs gap-1.5',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemLeadingChip: 'size-4',
                    itemLeadingChipSize: 'sm',
                    itemTrailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5',
                    label: 'p-1.5 text-xs gap-1.5',
                    item: 'p-1.5 text-sm gap-1.5',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemLeadingChip: 'size-5',
                    itemLeadingChipSize: 'md',
                    itemTrailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5',
                    label: 'p-2 text-xs gap-2',
                    item: 'p-2 text-sm gap-2',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemLeadingChip: 'size-5',
                    itemLeadingChipSize: 'md',
                    itemTrailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6',
                    label: 'p-2 text-sm gap-2',
                    item: 'p-2 text-base gap-2',
                    itemLeadingIcon: 'size-6',
                    itemLeadingAvatarSize: 'xs',
                    itemLeadingChip: 'size-6',
                    itemLeadingChipSize: 'lg',
                    itemTrailingIcon: 'size-6'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                },
                {
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/select-menu.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[SelectA select element to choose from a list of
options.](/components/select)[SeparatorSeparates content horizontally or
vertically.](/components/separator)

