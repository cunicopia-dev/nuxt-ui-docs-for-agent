<!-- source: https://ui.nuxt.com/components/content-search --> # ContentSearchPRO

[CommandPalette](/components/command-
palette)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/content/ContentSearch.vue)

A ready to use CommandPalette to add to your documentation.

[](/getting-started/content)This component is only available when the
`@nuxt/content` module is installed.

## Usage

The ContentSearch component extends the [CommandPalette](/components/command-
palette) component, so you can pass any property such as `icon`,
`placeholder`, etc.

Use the `files` and `navigation` props with the `files` and `navigation`
values you fetched using the `queryCollectionSearchSections` and
`queryCollectionNavigation` composables from `@nuxt/content`.

You can open the CommandPalette by pressing ` ``K`, by using the
[ContentSearchButton](/components/content-search-button) component or by using
the `useContentSearch` composable: `const { open } = useContentSearch()`.

### Shortcut

Use the `shortcut` prop to change the shortcut used in
[defineShortcuts](/composables/define-shortcuts) to open the ContentSearch
component. Defaults to `meta_k` (` ` `K`).

app.vue

    
    
    <template>
      <UApp>
        <ClientOnly>
          <LazyUContentSearch
            v-model:search-term="searchTerm"
            shortcut="meta_k"
            :files="files"
            :navigation="navigation"
            :fuse="{ resultLimit: 42 }"
          />
        </ClientOnly>
      </UApp>
    </template>
    

### Color Mode

By default, a group of commands will be added to the command palette so you
can switch between light and dark mode. This will only take effect if the
`colorMode` is not forced in a specific page which can be achieved through
`definePageMeta`:

pages/index.vue

    
    
    <script setup lang="ts">
    definePageMeta({
      colorMode: 'dark'
    })
    </script>
    

You can disable this behavior by setting the `color-mode` prop to `false`:

app.vue

    
    
    <template>
      <UApp>
        <ClientOnly>
          <LazyUContentSearch
            v-model:search-term="searchTerm"
            :color-mode="false"
            :files="files"
            :navigation="navigation"
            :fuse="{ resultLimit: 42 }"
          />
        </ClientOnly>
      </UApp>
    </template>
    

## Examples

### Within `app.vue`

Use the ContentSearch component in your `app.vue` or in a layout:

app.vue

    
    
    <script setup lang="ts">
    const { data: navigation } = await useAsyncData('navigation', () => queryCollectionNavigation('content'))
    const { data: files } = useLazyAsyncData('search', () => queryCollectionSearchSections('content'), {
      server: false
    })
    
    const links = [{
      label: 'Docs',
      icon: 'i-lucide-book',
      to: '/getting-started'
    }, {
      label: 'Components',
      icon: 'i-lucide-box',
      to: '/components'
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-chart-no-axes-gantt',
      to: '/roadmap'
    }]
    
    const searchTerm = ref('')
    </script>
    
    <template>
      <UApp>
        <ClientOnly>
          <LazyUContentSearch
            v-model:search-term="searchTerm"
            :files="files"
            shortcut="meta_k"
            :navigation="navigation"
            :links="links"
            :fuse="{ resultLimit: 42 }"
          />
        </ClientOnly>
      </UApp>
    </template>
    

It is recommended to wrap the `ContentSearch` component in a
[ClientOnly](https://nuxt.com/docs/api/components/client-only) component so
it's not rendered on the server.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`searchTerm`| | ` string`  
`icon`| `appConfig.ui.icons.search`| ` string`The icon displayed in the search
input.  
`placeholder`| | ` string`Placeholder for the command palette search input.  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`shortcut`| `'meta_k'`| ` string`Keyboard shortcut to open the search (used by
[`defineShortcuts`](https://ui.nuxt.com/composables/define-shortcuts))  
`links`| | ` ContentSearchLink[]`Links group displayed as the first group in the command palette.Show properties

  * `label?: string`
  * `description?: string`
  * `icon?: string`
  * `children?: ContentSearchLink[]`
  * `disabled?: boolean`
  * `class?: any`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `raw?: boolean`When `true`, only styles from `class`, `activeClass`, and `inactiveClass` will be applied.

  
`navigation`| | ` ContentNavigationItem[]`Show properties

  * `title: string`
  * `path: string`
  * `stem?: string`
  * `children?: ContentNavigationItem[]`
  * `page?: false`

  
`groups`| | ` CommandPaletteGroup<ContentSearchItem>[]`Custom groups displayed between navigation and color mode group.  
`files`| | ` ContentSearchFile[]`Show properties

  * `id: string`
  * `title: string`
  * `titles: string[]`
  * `level: number`
  * `content: string`

  
`fuse`| `{ fuseOptions: { includeMatches: true } }`| `
UseFuseOptions<ContentSearchLink>`Options for
[useFuse](https://vueuse.org/integrations/useFuse) passed to the
[CommandPalette](https://ui.nuxt.com/components/command-palette).  
`colorMode`| `true`| `boolean`When `true`, the theme command will be added to
the groups.  
`ui`| | ` { modal?: ClassNameValue; input?: ClassNameValue; } & { root?: ClassNameValue; input?: ClassNameValue; close?: ClassNameValue; ... 19 more ...; itemLabelSuffix?: ClassNameValue; }`Show properties

  * `modal?: ClassNameValue`
  * `input?: ClassNameValue`
  * `root?: ClassNameValue`
  * `close?: ClassNameValue`
  * `content?: ClassNameValue`
  * `viewport?: ClassNameValue`
  * `group?: ClassNameValue`
  * `empty?: ClassNameValue`
  * `label?: ClassNameValue`
  * `item?: ClassNameValue`
  * `itemLeadingIcon?: ClassNameValue`
  * `itemLeadingAvatar?: ClassNameValue`
  * `itemLeadingAvatarSize?: ClassNameValue`
  * `itemLeadingChip?: ClassNameValue`
  * `itemLeadingChipSize?: ClassNameValue`
  * `itemTrailing?: ClassNameValue`
  * `itemTrailingIcon?: ClassNameValue`
  * `itemTrailingHighlightedIcon?: ClassNameValue`
  * `itemTrailingKbds?: ClassNameValue`
  * `itemTrailingKbdsSize?: ClassNameValue`
  * `itemLabel?: ClassNameValue`
  * `itemLabelBase?: ClassNameValue`
  * `itemLabelPrefix?: ClassNameValue`
  * `itemLabelSuffix?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`empty`| `{ searchTerm?: string | undefined; }`  
`close`| `{ ui: { root: (props?: Record<string, any> | undefined) => string; input: (props?: Record<string, any> | undefined) => string; close: (props?: Record<string, any> | undefined) => string; ... 19 more ...; itemLabelSuffix: (props?: Record<...> | undefined) => string; }; }`  
`item`| `{ item: ContentSearchItem; index: number; }`  
`item-leading`| `{ item: ContentSearchItem; index: number; }`  
`item-label`| `{ item: ContentSearchItem; index: number; }`  
`item-trailing`| `{ item: ContentSearchItem; index: number; }`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:searchTerm`| `string`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        contentSearch: {
          slots: {
            modal: 'sm:max-w-3xl sm:h-[28rem]',
            input: '[&>input]:text-base/5'
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
          uiPro: {
            contentSearch: {
              slots: {
                modal: 'sm:max-w-3xl sm:h-[28rem]',
                input: '[&>input]:text-base/5'
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
          uiPro: {
            contentSearch: {
              slots: {
                modal: 'sm:max-w-3xl sm:h-[28rem]',
                input: '[&>input]:text-base/5'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ContentNavigationAn accordion-style navigation component for organizing page
links.](/components/content-navigation)[ContentSearchButtonA pre-styled Button
to open the ContentSearch modal.](/components/content-search-button)

