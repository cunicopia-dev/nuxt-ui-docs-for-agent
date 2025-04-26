<!-- source: https://ui.nuxt.com/components/command-palette --> # CommandPalette

[Fuse.js](https://fusejs.io/)[Combobox](https://reka-
ui.com/docs/components/combobox)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/CommandPalette.vue)

A command palette with full-text search powered by Fuse.js for efficient fuzzy
matching.

## Usage

Use the `v-model` directive to control the value of the CommandPalette or the
`default-value` prop to set the initial value when you do not need to control
its state.

You can also use the `@update:model-value` event to listen to the selected
item(s).

### Groups

The CommandPalette component filters groups and ranks matching commands by
relevance as users type. It provides dynamic, instant search results for
efficient command discovery. Use the `groups` prop as an array of objects with
the following properties:

  * `id: string`
  * `label?: string`
  * `slot?: string`
  * `items?: CommandPaletteItem[]`
  * `ignoreFilter?: boolean`
  * `postFilter?: (searchTerm: string, items: T[]) => T[]`
  * `highlightedIcon?: string`

You must provide an `id` for each group otherwise the group will be ignored.

Each group contains an `items` array of objects that define the commands. Each
item can have the following properties:

  * `prefix?: string`
  * `label?: string`
  * `suffix?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `chip?: ChipProps`
  * `kbds?: string[] | KbdProps[]`
  * `active?: boolean`
  * `loading?: boolean`
  * `disabled?: boolean`
  * `slot?: string`
  * `onSelect?(e?: Event): void`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

Users

![](https://github.com/benjamincanac.png)Benjamin
Canacbenjamincanac![](https://github.com/smarroufin.png)Sylvain
Marroufinsmarroufin![](https://github.com/atinux.png)Sébastien
Chopinatinux![](https://github.com/romhml.png)Romain
Hamelromhml![](https://github.com/Haythamasalama.png)Haytham A.
SalamaHaythamasalama![](https://github.com/danielroe.png)Daniel
Roedanielroe![](https://github.com/noook.png)Neil Richternoook

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'users',
        label: 'Users',
        items: [
          {
            label: 'Benjamin Canac',
            suffix: 'benjamincanac',
            avatar: {
              src: 'https://github.com/benjamincanac.png'
            }
          },
          {
            label: 'Sylvain Marroufin',
            suffix: 'smarroufin',
            avatar: {
              src: 'https://github.com/smarroufin.png'
            }
          },
          {
            label: 'Sébastien Chopin',
            suffix: 'atinux',
            avatar: {
              src: 'https://github.com/atinux.png'
            }
          },
          {
            label: 'Romain Hamel',
            suffix: 'romhml',
            avatar: {
              src: 'https://github.com/romhml.png'
            }
          },
          {
            label: 'Haytham A. Salama',
            suffix: 'Haythamasalama',
            avatar: {
              src: 'https://github.com/Haythamasalama.png'
            }
          },
          {
            label: 'Daniel Roe',
            suffix: 'danielroe',
            avatar: {
              src: 'https://github.com/danielroe.png'
            }
          },
          {
            label: 'Neil Richter',
            suffix: 'noook',
            avatar: {
              src: 'https://github.com/noook.png'
            }
          }
        ]
      }
    ])
    const value = ref({})
    </script>
    
    <template>
      <UCommandPalette v-model="value" :groups="groups" class="flex-1" />
    </template>
    

Expand code

### Multiple

Use the `multiple` prop to allow multiple selections.

Users

![](https://github.com/benjamincanac.png)Benjamin
Canacbenjamincanac![](https://github.com/smarroufin.png)Sylvain
Marroufinsmarroufin![](https://github.com/atinux.png)Sébastien
Chopinatinux![](https://github.com/romhml.png)Romain
Hamelromhml![](https://github.com/Haythamasalama.png)Haytham A.
SalamaHaythamasalama![](https://github.com/danielroe.png)Daniel
Roedanielroe![](https://github.com/noook.png)Neil Richternoook

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'users',
        label: 'Users',
        items: [
          {
            label: 'Benjamin Canac',
            suffix: 'benjamincanac',
            avatar: {
              src: 'https://github.com/benjamincanac.png'
            }
          },
          {
            label: 'Sylvain Marroufin',
            suffix: 'smarroufin',
            avatar: {
              src: 'https://github.com/smarroufin.png'
            }
          },
          {
            label: 'Sébastien Chopin',
            suffix: 'atinux',
            avatar: {
              src: 'https://github.com/atinux.png'
            }
          },
          {
            label: 'Romain Hamel',
            suffix: 'romhml',
            avatar: {
              src: 'https://github.com/romhml.png'
            }
          },
          {
            label: 'Haytham A. Salama',
            suffix: 'Haythamasalama',
            avatar: {
              src: 'https://github.com/Haythamasalama.png'
            }
          },
          {
            label: 'Daniel Roe',
            suffix: 'danielroe',
            avatar: {
              src: 'https://github.com/danielroe.png'
            }
          },
          {
            label: 'Neil Richter',
            suffix: 'noook',
            avatar: {
              src: 'https://github.com/noook.png'
            }
          }
        ]
      }
    ])
    const value = ref([])
    </script>
    
    <template>
      <UCommandPalette multiple v-model="value" :groups="groups" class="flex-1" />
    </template>
    

Expand code

Ensure to pass an array to the `default-value` prop or the `v-model`
directive.

### Placeholder

Use the `placeholder` prop to change the placeholder text.

placeholder

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette placeholder="Search an app..." :groups="groups" class="flex-1" />
    </template>
    

Expand code

### Icon

Use the `icon` prop to customize the input [Icon](/components/icon). Defaults
to `i-lucide-search`.

icon

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette icon="i-lucide-box" :groups="groups" class="flex-1" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.search` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.search` key.

### Loading

Use the `loading` prop to show a loading icon on the CommandPalette.

loading

true

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette loading :groups="groups" class="flex-1" />
    </template>
    

Expand code

### Loading Icon

Use the `loading-icon` prop to customize the loading icon. Defaults to
`i-lucide-refresh-cw`.

loading

true

loadingIcon

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette loading loading-icon="i-lucide-repeat-2" :groups="groups" class="flex-1" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.loading` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.loading` key.

### Disabled

Use the `disabled` prop to disable the CommandPalette.

disabled

true

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette disabled :groups="groups" class="flex-1" />
    </template>
    

Expand code

### Close

Use the `close` prop to display a [Button](/components/button) to dismiss the
CommandPalette.

An `update:open` event will be emitted when the close button is clicked.

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette close :groups="groups" class="flex-1" />
    </template>
    

Expand code

You can pass any property from the [Button](/components/button) component to
customize it.

close.class

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette
        :close="{
          color: 'primary',
          variant: 'outline',
          class: 'rounded-full'
        }"
        :groups="groups"
        class="flex-1"
      />
    </template>
    

Expand code

### Close Icon

Use the `close-icon` prop to customize the close button
[Icon](/components/icon). Defaults to `i-lucide-x`.

closeIcon

CalendarMusicMaps

    
    
    <script setup lang="ts">
    const groups = ref([
      {
        id: 'apps',
        items: [
          {
            label: 'Calendar',
            icon: 'i-lucide-calendar'
          },
          {
            label: 'Music',
            icon: 'i-lucide-music'
          },
          {
            label: 'Maps',
            icon: 'i-lucide-map'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UCommandPalette close close-icon="i-lucide-arrow-right" :groups="groups" class="flex-1" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

## Examples

### Control selected item(s)

You can control the selected item(s) by using the `default-value` prop or the
`v-model` directive, by using the `onSelect` field on each item or by using
the `@update:model-value` event.

Users

[![](https://github.com/benjamincanac.png)Benjamin
Canacbenjamincanac](https://github.com/benjamincanac)[![](https://github.com/smarroufin.png)Sylvain
Marroufinsmarroufin](https://github.com/smarroufin)[![](https://github.com/atinux.png)Sébastien
Chopinatinux](https://github.com/atinux)[![](https://github.com/romhml.png)Romain
Hamelromhml](https://github.com/romhml)[![](https://github.com/Haythamasalama.png)Haytham
A.
SalamaHaythamasalama](https://github.com/Haythamasalama)[![](https://github.com/danielroe.png)Daniel
Roedanielroe](https://github.com/danielroe)[![](https://github.com/noook.png)Neil
Richternoook](https://github.com/noook)

Add new fileCreate a new file in the current directory or workspace.` ``N`Add
new folderCreate a new folder in the current directory or workspace.` ``F`Add
hashtagAdd a hashtag to the current item.` ``H`Add labelAdd a label to the
current item.` ``L`

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    const groups = ref([
      {
        id: 'users',
        label: 'Users',
        items: [
          {
            label: 'Benjamin Canac',
            suffix: 'benjamincanac',
            to: 'https://github.com/benjamincanac',
            target: '_blank',
            avatar: {
              src: 'https://github.com/benjamincanac.png'
            }
          },
          {
            label: 'Sylvain Marroufin',
            suffix: 'smarroufin',
            to: 'https://github.com/smarroufin',
            target: '_blank',
            avatar: {
              src: 'https://github.com/smarroufin.png'
            }
          },
          {
            label: 'Sébastien Chopin',
            suffix: 'atinux',
            to: 'https://github.com/atinux',
            target: '_blank',
            avatar: {
              src: 'https://github.com/atinux.png'
            }
          },
          {
            label: 'Romain Hamel',
            suffix: 'romhml',
            to: 'https://github.com/romhml',
            target: '_blank',
            avatar: {
              src: 'https://github.com/romhml.png'
            }
          },
          {
            label: 'Haytham A. Salama',
            suffix: 'Haythamasalama',
            to: 'https://github.com/Haythamasalama',
            target: '_blank',
            avatar: {
              src: 'https://github.com/Haythamasalama.png'
            }
          },
          {
            label: 'Daniel Roe',
            suffix: 'danielroe',
            to: 'https://github.com/danielroe',
            target: '_blank',
            avatar: {
              src: 'https://github.com/danielroe.png'
            }
          },
          {
            label: 'Neil Richter',
            suffix: 'noook',
            to: 'https://github.com/noook',
            target: '_blank',
            avatar: {
              src: 'https://github.com/noook.png'
            }
          }
        ]
      },
      {
        id: 'actions',
        items: [
          {
            label: 'Add new file',
            suffix: 'Create a new file in the current directory or workspace.',
            icon: 'i-lucide-file-plus',
            kbds: [
              'meta',
              'N'
            ],
            onSelect() {
              toast.add({ title: 'Add new file' })
            }
          },
          {
            label: 'Add new folder',
            suffix: 'Create a new folder in the current directory or workspace.',
            icon: 'i-lucide-folder-plus',
            kbds: [
              'meta',
              'F'
            ],
            onSelect() {
              toast.add({ title: 'Add new folder' })
            }
          },
          {
            label: 'Add hashtag',
            suffix: 'Add a hashtag to the current item.',
            icon: 'i-lucide-hash',
            kbds: [
              'meta',
              'H'
            ],
            onSelect() {
              toast.add({ title: 'Add hashtag' })
            }
          },
          {
            label: 'Add label',
            suffix: 'Add a label to the current item.',
            icon: 'i-lucide-tag',
            kbds: [
              'meta',
              'L'
            ],
            onSelect() {
              toast.add({ title: 'Add label' })
            }
          }
        ]
      }
    ])
    
    function onSelect(item: any) {
      console.log(item)
    }
    </script>
    
    <template>
      <UCommandPalette
        :groups="groups"
        class="flex-1 h-80"
        @update:model-value="onSelect"
      />
    </template>
    

Expand code

### Control search term

Use the `v-model:search-term` directive to control the search term.

[![](https://github.com/benjamincanac.png)Benjamin
Canacbenjamincanac](https://github.com/benjamincanac)[![](https://github.com/atinux.png)Sébastien
Chopinatinux](https://github.com/atinux)

    
    
    <script setup lang="ts">
    const users = [
      {
        label: 'Benjamin Canac',
        suffix: 'benjamincanac',
        to: 'https://github.com/benjamincanac',
        target: '_blank',
        avatar: {
          src: 'https://github.com/benjamincanac.png'
        }
      },
      {
        label: 'Sylvain Marroufin',
        suffix: 'smarroufin',
        to: 'https://github.com/smarroufin',
        target: '_blank',
        avatar: {
          src: 'https://github.com/smarroufin.png'
        }
      },
      {
        label: 'Sébastien Chopin',
        suffix: 'atinux',
        to: 'https://github.com/atinux',
        target: '_blank',
        avatar: {
          src: 'https://github.com/atinux.png'
        }
      },
      {
        label: 'Romain Hamel',
        suffix: 'romhml',
        to: 'https://github.com/romhml',
        target: '_blank',
        avatar: {
          src: 'https://github.com/romhml.png'
        }
      },
      {
        label: 'Haytham A. Salama',
        suffix: 'Haythamasalama',
        to: 'https://github.com/Haythamasalama',
        target: '_blank',
        avatar: {
          src: 'https://github.com/Haythamasalama.png'
        }
      },
      {
        label: 'Daniel Roe',
        suffix: 'danielroe',
        to: 'https://github.com/danielroe',
        target: '_blank',
        avatar: {
          src: 'https://github.com/danielroe.png'
        }
      },
      {
        label: 'Neil Richter',
        suffix: 'noook',
        to: 'https://github.com/noook',
        target: '_blank',
        avatar: {
          src: 'https://github.com/noook.png'
        }
      }
    ]
    
    const searchTerm = ref('B')
    
    function onSelect() {
      searchTerm.value = ''
    }
    </script>
    
    <template>
      <UCommandPalette
        v-model:search-term="searchTerm"
        :groups="[{ id: 'users', items: users }]"
        class="flex-1"
        @update:model-value="onSelect"
      />
    </template>
    

Expand code

This example uses the `@update:model-value` event to reset the search term
when an item is selected.

### With fetched items

You can fetch items from an API and use them in the CommandPalette.

Users

![](https://i.pravatar.cc/120?img=1)Leanne Graham[[email protected]](/cdn-
cgi/l/email-protection)![](https://i.pravatar.cc/120?img=2)Ervin Howell[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=3)Clementine Bauch[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=4)Patricia Lebsack[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=5)Chelsey Dietrich[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=6)Mrs. Dennis Schulist[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=7)Kurtis Weissnat[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=8)Nicholas Runolfsdottir V[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=9)Glenna Reichert[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=10)Clementina DuBuque[[email
protected]](/cdn-cgi/l/email-protection)

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || []
    }])
    </script>
    
    <template>
      <UCommandPalette
        v-model:search-term="searchTerm"
        :loading="status === 'pending'"
        :groups="groups"
        class="flex-1 h-80"
      />
    </template>
    

Expand code

### With ignore filter

You can set the `ignoreFilter` field to `true` on a group to disable the
internal search and use your own search logic.

Users

![](https://i.pravatar.cc/120?img=1)Leanne Graham[[email protected]](/cdn-
cgi/l/email-protection)![](https://i.pravatar.cc/120?img=2)Ervin Howell[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=3)Clementine Bauch[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=4)Patricia Lebsack[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=5)Chelsey Dietrich[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=6)Mrs. Dennis Schulist[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=7)Kurtis Weissnat[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=8)Nicholas Runolfsdottir V[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=9)Glenna Reichert[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=10)Clementina DuBuque[[email
protected]](/cdn-cgi/l/email-protection)

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    const searchTermDebounced = refDebounced(searchTerm, 200)
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      params: { q: searchTermDebounced },
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || [],
      ignoreFilter: true
    }])
    </script>
    
    <template>
      <UCommandPalette
        v-model:search-term="searchTerm"
        :loading="status === 'pending'"
        :groups="groups"
        class="flex-1 h-80"
      />
    </template>
    

Expand code

This example uses
[`refDebounced`](https://vueuse.org/shared/refDebounced/#refdebounced) to
debounce the API calls.

### With post-filtered items

You can use the `postFilter` field on a group to filter items after the search
happened.

IntroductionInstallation

    
    
    <script setup lang="ts">
    const items = [
      {
        id: '/',
        label: 'Introduction',
        level: 1
      },
      {
        id: '/getting-started#whats-new-in-v3',
        label: 'What\'s new in v3?',
        level: 2
      },
      {
        id: '/getting-started#reka-ui',
        label: 'Reka UI',
        level: 3
      },
      {
        id: '/getting-started#tailwind-css-v4',
        label: 'Tailwind CSS v4',
        level: 3
      },
      {
        id: '/getting-started#tailwind-variants',
        label: 'Tailwind Variants',
        level: 3
      },
      {
        id: '/getting-started/installation',
        label: 'Installation',
        level: 1
      }
    ]
    
    function postFilter(searchTerm: string, items: any[]) {
      // Filter only first level items if no searchTerm
      if (!searchTerm) {
        return items?.filter(item => item.level === 1)
      }
    
      return items
    }
    </script>
    
    <template>
      <UCommandPalette :groups="[{ id: 'files', items, postFilter }]" class="flex-1" />
    </template>
    

Expand code

Start typing to see items with higher level appear.

### With custom fuse search

You can use the `fuse` prop to override the options of
[useFuse](https://vueuse.org/integrations/useFuse) which defaults to:

    
    
    {
      fuseOptions: {
        ignoreLocation: true,
        threshold: 0.1,
        keys: ['label', 'suffix']
      },
      resultLimit: 12,
      matchAllWhenSearchEmpty: true
    }
    

The `fuseOptions` are the options of
[Fuse.js](https://www.fusejs.io/api/options.html), the `resultLimit` is the
maximum number of results to return and the `matchAllWhenSearchEmpty` is a
boolean to match all items when the search term is empty.

You can for example set `{ fuseOptions: { includeMatches: true } }` to
highlight the search term in the items.

![](https://i.pravatar.cc/120?img=1)Leanne Graham[[email protected]](/cdn-
cgi/l/email-protection)![](https://i.pravatar.cc/120?img=2)Ervin Howell[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=3)Clementine Bauch[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=4)Patricia Lebsack[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=5)Chelsey Dietrich[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=6)Mrs. Dennis Schulist[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=7)Kurtis Weissnat[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=8)Nicholas Runolfsdottir V[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=9)Glenna Reichert[[email
protected]](/cdn-cgi/l/email-
protection)![](https://i.pravatar.cc/120?img=10)Clementina DuBuque[[email
protected]](/cdn-cgi/l/email-protection)

    
    
    <script setup lang="ts">
    const { data: users } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    </script>
    
    <template>
      <UCommandPalette
        :groups="[{ id: 'users', items: users || [] }]"
        :fuse="{ fuseOptions: { includeMatches: true } }"
        class="flex-1 h-80"
      />
    </template>
    

Expand code

### Within a Popover

You can use the CommandPalette component inside a
[Popover](/components/popover)'s content.

Select labels

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'bug',
        value: 'bug',
        chip: {
          color: 'error' as const
        }
      },
      {
        label: 'feature',
        value: 'feature',
        chip: {
          color: 'success' as const
        }
      },
      {
        label: 'enhancement',
        value: 'enhancement',
        chip: {
          color: 'info' as const
        }
      }
    ])
    const label = ref([])
    </script>
    
    <template>
      <UPopover :content="{ side: 'right', align: 'start' }">
        <UButton
          icon="i-lucide-tag"
          label="Select labels"
          color="neutral"
          variant="subtle"
        />
    
        <template #content>
          <UCommandPalette
            v-model="label"
            multiple
            placeholder="Search labels..."
            :groups="[{ id: 'labels', items }]"
            :ui="{ input: '[&>input]:h-8 [&>input]:text-sm' }"
          />
        </template>
      </UPopover>
    </template>
    

Expand code

### Within a Modal

You can use the CommandPalette component inside a [Modal](/components/modal)'s
content.

Search users...

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      params: { q: searchTerm },
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || [],
      ignoreFilter: true
    }])
    </script>
    
    <template>
      <UModal>
        <UButton
          label="Search users..."
          color="neutral"
          variant="subtle"
          icon="i-lucide-search"
        />
    
        <template #content>
          <UCommandPalette
            v-model:search-term="searchTerm"
            :loading="status === 'pending'"
            :groups="groups"
            placeholder="Search users..."
            class="h-80"
          />
        </template>
      </UModal>
    </template>
    

Expand code

### Within a Drawer

You can use the CommandPalette component inside a
[Drawer](/components/drawer)'s content.

Search users...

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      params: { q: searchTerm },
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || [],
      ignoreFilter: true
    }])
    </script>
    
    <template>
      <UDrawer :handle="false">
        <UButton
          label="Search users..."
          color="neutral"
          variant="subtle"
          icon="i-lucide-search"
        />
    
        <template #content>
          <UCommandPalette
            v-model:search-term="searchTerm"
            :loading="status === 'pending'"
            :groups="groups"
            placeholder="Search users..."
            class="h-80"
          />
        </template>
      </UDrawer>
    </template>
    

Expand code

### Listen open state

When using the `close` prop, you can listen to the `update:open` event when
the button is clicked.

Search users...

    
    
    <script setup lang="ts">
    const open = ref(false)
    
    const users = [
      {
        label: 'Benjamin Canac',
        suffix: 'benjamincanac',
        to: 'https://github.com/benjamincanac',
        target: '_blank',
        avatar: {
          src: 'https://github.com/benjamincanac.png'
        }
      },
      {
        label: 'Sylvain Marroufin',
        suffix: 'smarroufin',
        to: 'https://github.com/smarroufin',
        target: '_blank',
        avatar: {
          src: 'https://github.com/smarroufin.png'
        }
      },
      {
        label: 'Sébastien Chopin',
        suffix: 'atinux',
        to: 'https://github.com/atinux',
        target: '_blank',
        avatar: {
          src: 'https://github.com/atinux.png'
        }
      },
      {
        label: 'Romain Hamel',
        suffix: 'romhml',
        to: 'https://github.com/romhml',
        target: '_blank',
        avatar: {
          src: 'https://github.com/romhml.png'
        }
      },
      {
        label: 'Haytham A. Salama',
        suffix: 'Haythamasalama',
        to: 'https://github.com/Haythamasalama',
        target: '_blank',
        avatar: {
          src: 'https://github.com/Haythamasalama.png'
        }
      },
      {
        label: 'Daniel Roe',
        suffix: 'danielroe',
        to: 'https://github.com/danielroe',
        target: '_blank',
        avatar: {
          src: 'https://github.com/danielroe.png'
        }
      },
      {
        label: 'Neil Richter',
        suffix: 'noook',
        to: 'https://github.com/noook',
        target: '_blank',
        avatar: {
          src: 'https://github.com/noook.png'
        }
      }
    ]
    </script>
    
    <template>
      <UModal v-model:open="open">
        <UButton
          label="Search users..."
          color="neutral"
          variant="subtle"
          icon="i-lucide-search"
        />
    
        <template #content>
          <UCommandPalette close :groups="[{ id: 'users', items: users }]" @update:open="open = $event" />
        </template>
      </UModal>
    </template>
    

Expand code

This can be useful when using the CommandPalette inside a
[`Modal`](/components/modal) for example.

### With custom slot

Use the `slot` property to customize a specific item or group.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-leading`
  * `#{{ item.slot }}-label`
  * `#{{ item.slot }}-trailing`
  * `#{{ group.slot }}`
  * `#{{ group.slot }}-leading`
  * `#{{ group.slot }}-label`
  * `#{{ group.slot }}-trailing`

Profile` ``P`Billing  50% off ` ``B`NotificationsSecurity

Users

[![](https://github.com/benjamincanac.png)Benjamin
Canacbenjamincanac](https://github.com/benjamincanac)[![](https://github.com/smarroufin.png)Sylvain
Marroufinsmarroufin](https://github.com/smarroufin)[![](https://github.com/atinux.png)Sébastien
Chopinatinux](https://github.com/atinux)[![](https://github.com/romhml.png)Romain
Hamelromhml](https://github.com/romhml)[![](https://github.com/Haythamasalama.png)Haytham
A.
SalamaHaythamasalama](https://github.com/Haythamasalama)[![](https://github.com/danielroe.png)Daniel
Roedanielroe](https://github.com/danielroe)[![](https://github.com/noook.png)Neil
Richternoook](https://github.com/noook)

    
    
    <script setup lang="ts">
    const groups = [
      {
        id: 'settings',
        items: [
          {
            label: 'Profile',
            icon: 'i-lucide-user',
            kbds: ['meta', 'P']
          },
          {
            label: 'Billing',
            icon: 'i-lucide-credit-card',
            kbds: ['meta', 'B'],
            slot: 'billing' as const
          },
          {
            label: 'Notifications',
            icon: 'i-lucide-bell'
          },
          {
            label: 'Security',
            icon: 'i-lucide-lock'
          }
        ]
      },
      {
        id: 'users',
        label: 'Users',
        slot: 'users' as const,
        items: [
          {
            label: 'Benjamin Canac',
            suffix: 'benjamincanac',
            to: 'https://github.com/benjamincanac',
            target: '_blank'
          },
          {
            label: 'Sylvain Marroufin',
            suffix: 'smarroufin',
            to: 'https://github.com/smarroufin',
            target: '_blank'
          },
          {
            label: 'Sébastien Chopin',
            suffix: 'atinux',
            to: 'https://github.com/atinux',
            target: '_blank'
          },
          {
            label: 'Romain Hamel',
            suffix: 'romhml',
            to: 'https://github.com/romhml',
            target: '_blank'
          },
          {
            label: 'Haytham A. Salama',
            suffix: 'Haythamasalama',
            to: 'https://github.com/Haythamasalama',
            target: '_blank'
          },
          {
            label: 'Daniel Roe',
            suffix: 'danielroe',
            to: 'https://github.com/danielroe',
            target: '_blank'
          },
          {
            label: 'Neil Richter',
            suffix: 'noook',
            to: 'https://github.com/noook',
            target: '_blank'
          }
        ]
      }
    ]
    </script>
    
    <template>
      <UCommandPalette :groups="groups" class="flex-1 h-80">
        <template #users-leading="{ item }">
          <UAvatar :src="`https://github.com/${item.suffix}.png`" size="2xs" />
        </template>
    
        <template #billing-label="{ item }">
          {{ item.label }}
    
          <UBadge variant="subtle" size="sm">
            50% off
          </UBadge>
        </template>
      </UCommandPalette>
    </template>
    

You can also use the `#item`, `#item-leading`, `#item-label` and `#item-
trailing` slots to customize all items.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`icon`| `appConfig.ui.icons.search`| ` string`The icon displayed in the input.  
`selectedIcon`| `appConfig.ui.icons.check`| ` string`The icon displayed when
an item is selected.  
`placeholder`| `t('commandPalette.placeholder')`| ` string`The placeholder
text for the input.  
`autofocus`| `true`| `boolean`Automatically focus the input when component is
mounted.  
`close`| `false`| `boolean | Partial<ButtonProps>`Display a close button in the input (useful when inside a Modal for example). `{ size: 'md', color: 'neutral', variant: 'ghost' }`  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`groups`| | ` CommandPaletteGroup<CommandPaletteItem>[]`  
`fuse`| `{ fuseOptions: { ignoreLocation: true, threshold: 0.1, keys:
['label', 'suffix'] }, resultLimit: 12, matchAllWhenSearchEmpty: true }`| `
UseFuseOptions<CommandPaletteItem>`Options for
[useFuse](https://vueuse.org/integrations/useFuse).  
`labelKey`| `'label'`| ` string`The key used to get the label from the item.  
`multiple`| | `boolean`Whether multiple options can be selected or not.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with listbox  
`modelValue`| `''`| ` null | string | number | Record<string, any> | AcceptableValue[]`The controlled value of the listbox. Can be binded with with `v-model`.  
`defaultValue`| | ` null | string | number | Record<string, any> | AcceptableValue[]`The value of the listbox when initially rendered. Use when you do not need to control the state of the Listbox  
`highlightOnHover`| | `boolean`When `true`, hover over item will trigger highlight  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`searchTerm`| `''`| ` string`  
`ui`| | ` { root?: ClassNameValue; input?: ClassNameValue; close?: ClassNameValue; content?: ClassNameValue; viewport?: ClassNameValue; ... 17 more ...; itemLabelSuffix?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`empty`| `{ searchTerm?: string | undefined; }`  
`close`| `{ ui: { root: (props?: Record<string, any> | undefined) => string; input: (props?: Record<string, any> | undefined) => string; close: (props?: Record<string, any> | undefined) => string; ... 19 more ...; itemLabelSuffix: (props?: Record<...> | undefined) => string; }; }`  
`item`| `{ item: CommandPaletteItem; index: number; }`  
`item-leading`| `{ item: CommandPaletteItem; index: number; }`  
`item-label`| `{ item: CommandPaletteItem; index: number; }`  
`item-trailing`| `{ item: CommandPaletteItem; index: number; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[value: CommandPaletteItem]`  
`highlight`| `[payload: { ref: HTMLElement; value: CommandPaletteItem; } | undefined]`  
`entryFocus`| `[event: CustomEvent<any>]`  
`leave`| `[event: Event]`  
`update:open`| `[value: boolean]`  
`update:searchTerm`| `[value: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        commandPalette: {
          slots: {
            root: 'flex flex-col min-h-0 min-w-0 divide-y divide-default',
            input: '[&>input]:h-12',
            close: '',
            content: 'relative overflow-hidden flex flex-col',
            viewport: 'relative divide-y divide-default scroll-py-1 overflow-y-auto flex-1 focus:outline-none',
            group: 'p-1 isolate',
            empty: 'py-6 text-center text-sm text-muted',
            label: 'p-1.5 text-xs font-semibold text-highlighted',
            item: 'group relative w-full flex items-center gap-1.5 p-1.5 text-sm select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
            itemLeadingIcon: 'shrink-0 size-5',
            itemLeadingAvatar: 'shrink-0',
            itemLeadingAvatarSize: '2xs',
            itemLeadingChip: 'shrink-0 size-5',
            itemLeadingChipSize: 'md',
            itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            itemTrailingIcon: 'shrink-0 size-5',
            itemTrailingHighlightedIcon: 'shrink-0 size-5 text-dimmed hidden group-data-highlighted:inline-flex',
            itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0 gap-0.5',
            itemTrailingKbdsSize: 'md',
            itemLabel: 'truncate space-x-1 rtl:space-x-reverse text-dimmed',
            itemLabelBase: 'text-highlighted [&>mark]:text-inverted [&>mark]:bg-primary',
            itemLabelPrefix: 'text-default',
            itemLabelSuffix: 'text-dimmed [&>mark]:text-inverted [&>mark]:bg-primary'
          },
          variants: {
            active: {
              true: {
                item: 'text-highlighted before:bg-elevated',
                itemLeadingIcon: 'text-default'
              },
              false: {
                item: [
                  'text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ],
                itemLeadingIcon: [
                  'text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
                  'transition-colors'
                ]
              }
            },
            loading: {
              true: {
                itemLeadingIcon: 'animate-spin'
              }
            }
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
            commandPalette: {
              slots: {
                root: 'flex flex-col min-h-0 min-w-0 divide-y divide-default',
                input: '[&>input]:h-12',
                close: '',
                content: 'relative overflow-hidden flex flex-col',
                viewport: 'relative divide-y divide-default scroll-py-1 overflow-y-auto flex-1 focus:outline-none',
                group: 'p-1 isolate',
                empty: 'py-6 text-center text-sm text-muted',
                label: 'p-1.5 text-xs font-semibold text-highlighted',
                item: 'group relative w-full flex items-center gap-1.5 p-1.5 text-sm select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
                itemLeadingIcon: 'shrink-0 size-5',
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '2xs',
                itemLeadingChip: 'shrink-0 size-5',
                itemLeadingChipSize: 'md',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0 size-5',
                itemTrailingHighlightedIcon: 'shrink-0 size-5 text-dimmed hidden group-data-highlighted:inline-flex',
                itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0 gap-0.5',
                itemTrailingKbdsSize: 'md',
                itemLabel: 'truncate space-x-1 rtl:space-x-reverse text-dimmed',
                itemLabelBase: 'text-highlighted [&>mark]:text-inverted [&>mark]:bg-primary',
                itemLabelPrefix: 'text-default',
                itemLabelSuffix: 'text-dimmed [&>mark]:text-inverted [&>mark]:bg-primary'
              },
              variants: {
                active: {
                  true: {
                    item: 'text-highlighted before:bg-elevated',
                    itemLeadingIcon: 'text-default'
                  },
                  false: {
                    item: [
                      'text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    itemLeadingIcon: [
                      'text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
                      'transition-colors'
                    ]
                  }
                },
                loading: {
                  true: {
                    itemLeadingIcon: 'animate-spin'
                  }
                }
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
            commandPalette: {
              slots: {
                root: 'flex flex-col min-h-0 min-w-0 divide-y divide-default',
                input: '[&>input]:h-12',
                close: '',
                content: 'relative overflow-hidden flex flex-col',
                viewport: 'relative divide-y divide-default scroll-py-1 overflow-y-auto flex-1 focus:outline-none',
                group: 'p-1 isolate',
                empty: 'py-6 text-center text-sm text-muted',
                label: 'p-1.5 text-xs font-semibold text-highlighted',
                item: 'group relative w-full flex items-center gap-1.5 p-1.5 text-sm select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
                itemLeadingIcon: 'shrink-0 size-5',
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '2xs',
                itemLeadingChip: 'shrink-0 size-5',
                itemLeadingChipSize: 'md',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0 size-5',
                itemTrailingHighlightedIcon: 'shrink-0 size-5 text-dimmed hidden group-data-highlighted:inline-flex',
                itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0 gap-0.5',
                itemTrailingKbdsSize: 'md',
                itemLabel: 'truncate space-x-1 rtl:space-x-reverse text-dimmed',
                itemLabelBase: 'text-highlighted [&>mark]:text-inverted [&>mark]:bg-primary',
                itemLabelPrefix: 'text-default',
                itemLabelSuffix: 'text-dimmed [&>mark]:text-inverted [&>mark]:bg-primary'
              },
              variants: {
                active: {
                  true: {
                    item: 'text-highlighted before:bg-elevated',
                    itemLeadingIcon: 'text-default'
                  },
                  false: {
                    item: [
                      'text-default data-highlighted:not-data-disabled:text-highlighted data-highlighted:not-data-disabled:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    itemLeadingIcon: [
                      'text-dimmed group-data-highlighted:not-group-data-disabled:text-default',
                      'transition-colors'
                    ]
                  }
                },
                loading: {
                  true: {
                    itemLeadingIcon: 'animate-spin'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[ColorPickerA component to select a color.](/components/color-
picker)[ContainerA container lets you center and constrain the width of your
content.](/components/container)

